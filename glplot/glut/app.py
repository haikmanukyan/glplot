import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ..glfw.camera import Camera

from numpy import *

class Event:
    def __init__(self):
        self.listeners = []
    def __add__(self, callback):
        self.listeners.append(callback)
        return self
    def __call__(self, *argv):
        for callback in self.listeners:
            callback(*argv)

class App:
    def __init__(self, camera = None, update = None, draw = None, window_size = (600,600), bg_color = None, name = "OpenGL App"):
        self.name = name

        if camera is None: self.camera = Camera(self)
        else: self.camera = camera
        self.is_paused = True
        self.is_mouse_down = False

        self.keys = dict([[(chr(i)),False] for i in range(256)])

        self.window_size = window_size
        self.aspect_ratio = window_size[0] / window_size[1]
        # self.bg_color = (0.3, 0.5, 0.9, 1.0) if bg_color is None else bg_color
        self.bg_color = (1.0, 1.0, 1.0, 1.0) if bg_color is None else bg_color

        self.onClick = Event()
        self.onKeyDown = Event()
        self.onKeyUp = Event()
        self.onScroll = Event()
        self.onMouseMove = Event()
        self.onMouseDrag = Event()
        self.draw = Event()
        self.update = Event()

        self.record = False
        self.save_path = 'data/captures/'
        self.overwrite = False
        self.fps = 50.
        self.last_time = 0
        self.button = -1
        if update is not None: self.update += update
        if draw is not None: self.update += draw

# ========== Recording ===========
    def capture(self):
        image_folder = self.save_path + "images/"
        raw = glReadPixels(0, 0, self.window_size[0], self.window_size[1], GL_RGB, GL_UNSIGNED_BYTE)
        image = Image.frombytes("RGB", (self.window_size[0], self.window_size[1]), raw).transpose(Image.FLIP_TOP_BOTTOM)
        
        if not self.overwrite:
            existing = [x for x in os.listdir(image_folder) if x.startswith(self.name)]
            path = f'{image_folder}{self.name}-{len(existing)}.png'
        else:
            path = f'{image_folder}{self.name}.png'
        image.save(path)

    def start_recording(self):
        self.record = True
        video_folder = self.save_path + "videos/"

        if not self.overwrite:
            existing = [x for x in os.listdir(video_folder) if x.startswith(self.name)]
            path = f'{video_folder}{self.name}-{len(existing)}.mp4'
        else:
            path = f'{video_folder}{self.name}.mp4'
        fourcc = cv2.VideoWriter_fourcc(*'H264')
        # fourcc = cv2.VideoWriter_fourcc(*'MP4V') 
        self.writer = cv2.VideoWriter(path, fourcc, 50.0, (self.window_size[0],self.window_size[1]))

    def stop_recording(self):
        self.record = False
        self.writer.release()

    # ======== Physics ==========
    def raycast(self):
        m_y, m_x = glutGet(GLUT_WINDOW_HEIGHT) - self.m_y, self.m_x
        m_z = glReadPixels(m_x, m_y, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT)
        return gluUnProject(m_x, m_y, m_z)

    # ========= Mouse ===========
    def passive(self, m_x, m_y):
        self.onMouseMove(m_x, m_y)
        self.m_x, self.m_y = m_x, m_y

    def active(self, m_x, m_y):
        self.camera.onMouseDrag(self, m_x, m_y)
        self.onMouseDrag(self, m_x, m_y)
        self.m_x, self.m_y = m_x, m_y

    def scroll(self, wheel, direction, m_x, m_y):
        self.camera.onScroll(self, wheel, direction, m_x, m_y)
        self.onScroll(self, wheel, direction, m_x, m_y)
    
    def mouseFunc(self, button, state, mouse_x, mouse_y):
        self.button = button
        self.onClick(self, button, state, mouse_x, mouse_y)
    
    # =========== Keyboard ==========
    def keyFunc(self, key, x, y):
        if isinstance(key, bytes): key = key.decode()
        if key == 'p' or key == ' ': self.is_paused = not self.is_paused
        if key == 'r':
            if not self.record: self.start_recording()
            else: self.stop_recording()
        if key == 'c':
            self.capture()

        self.keys[key] = True
        self.onKeyDown(self, key, x, y)

    def specialUpFunc(self, key, x, y):
        if key == GLUT_KEY_F1:
            self.camera.euler = [0., pi, 0.]
        if key == GLUT_KEY_F2:
            self.camera.euler = [0., pi / 2, 0.]
        if key == GLUT_KEY_F3:
            print (self.camera.euler)
            self.camera.euler = [pi / 2, pi / 2, 0.]

    def keyUpFunc(self, key, x, y):
        key = key.decode()
        self.keys[key] = False
        self.onKeyUp(self, key, x, y)

    # ========== Update =============
    def idleFunc(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_time
        wait_time = max(0, 1 / self.fps - elapsed_time)
        time.sleep(wait_time)
        self.last_time = current_time
        glutPostRedisplay()

    def displayFunc(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        self.camera.update(self)
        self.draw(self)
        self.update(self)
        self.camera.update_view()

        if self.record:
            raw = glReadPixels(0, 0, self.window_size[0], self.window_size[1], GL_RGB, GL_UNSIGNED_BYTE)
            image = uint8(Image.frombytes("RGB", (self.window_size[0], self.window_size[1]), raw))[::-1,:,[2,1,0]]
            self.writer.write(image)           

        glutSwapBuffers()
    
    # ========= Glut ==========
    def init(self):
        glutInit()
        glutInitWindowSize(*self.window_size)

        glutSetKeyRepeat(False)
        glutCreateWindow(self.name)
        glutSetCursor(GLUT_CURSOR_SPRAY)
        glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_CONTINUE_EXECUTION)

        glClearColor(*self.bg_color)
        glEnable(GL_DEPTH_TEST)

        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, self.aspect_ratio, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def set_bg(self, *color):
        glClearColor(*color)
        self.bg_color = color

    def reshapeFunc(self, w, h):
        h = max(h,1)
        ratio = w / h

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glViewport(0, 0, w, h)
        gluPerspective(45,ratio,1,1000)
        glMatrixMode(GL_MODELVIEW)

    def run(self):
        self.init()
        self.last_time = time.time()

        glutDisplayFunc(self.displayFunc)
        glutMouseFunc(self.mouseFunc)
        glutIdleFunc(self.idleFunc)
        glutKeyboardUpFunc(self.keyUpFunc)
        glutKeyboardFunc(self.keyFunc)
        glutSpecialUpFunc(self.specialUpFunc)
        # glutSpecialFunc(self.keyFunc)
        glutMotionFunc(self.active)
        glutPassiveMotionFunc(self.passive)
        glutMouseWheelFunc(self.scroll)
        glutReshapeFunc(self.reshapeFunc)
        glutMainLoop()


if __name__ == "__main__":
    from .gl import gldraw as draw

    def update(self):
        draw.draw_ground()

    app = App()
    app.update += update
    app.run()
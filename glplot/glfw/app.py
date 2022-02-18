import glfw
from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *

from glplot.gl.event import Event
from glplot.gl import gldraw
from glplot.glfw.camera import Camera

class App:
    def __init__(self, canvas) -> None:
        self.init_glfw()
        self.init_events()
        self.init_window()
        self.init_camera()
        self.init_mouse()
        self.init_lighting()

        self.canvas = canvas


    def init_lighting(self):
        # glLight(GL_LIGHT0, GL_POSITION,  (0,0,5,1))  # point light
        glLightfv(GL_LIGHT0, GL_AMBIENT, (1,1,1,1))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1,1,1,1))
        
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)

    def init_mouse(self):
        self.xpos = 0
        self.ypos = 0
        self.onMouseMove += self.mouseMoveCallback
        self.button = 0

    def mouseMoveCallback(self, window, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def init_camera(self):
        self.camera = Camera(self)
        self.onScroll += self.camera.onScroll
        self.onMouseMove += self.camera.onMouseDrag

    def init_glfw(self):
        if not glfw.init(): return
        self.window = glfw.create_window(800, 800, "GLPlot", None, None)
        if not self.window: glfw.terminate()
        glfw.make_context_current(self.window)

    def init_window(self):
        glClearColor(1.0,1.0,1.0,1.0)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, 1., 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)


    def init_events(self):
        self.onClick = Event()
        self.onKeyUp = Event()
        self.onKeyDown = Event()
        self.onScroll = Event()
        self.onMouseMove = Event()

        glfwSetCursorPosCallback(self.window, self.onMouseMove)        
        glfwSetScrollCallback(self.window, self.onScroll)

    def run(self):
        while not glfw.window_should_close(self.window):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            self.canvas.draw()
            self.canvas.update()

            self.camera.update_view()
            glfw.swap_buffers(self.window)
            glfw.poll_events()

        glfw.terminate()
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

from OpenGL.GLUT.fonts import GLUT_STROKE_ROMAN

def idle():
    time.sleep(0.01)
    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor(1,1,1)
    # glBegin(GL_TRIANGLES)
    # glVertex3f(0,0,0)
    # glVertex3f(0,800,0)
    # glVertex3f(800,0,0)
    # glEnd()
    glLineWidth(5)
    glLoadIdentity()
    glutStrokeString(GLUT_STROKE_ROMAN, "LKJ".encode())
    glutSwapBuffers()

glutInit()
glutInitWindowSize(800,800)
glutCreateWindow("A")

glEnable(GL_DEPTH_TEST)
glClearColor(0.3, 0.5, 0.9, 1.0)
glMatrixMode(GL_PROJECTION)
gluOrtho2D(0,800,0,800)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

glutIdleFunc(idle)
glutDisplayFunc(display)
glutMainLoop()
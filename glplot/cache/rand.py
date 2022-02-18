from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

def idle():
    time.sleep(0.01)
    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glColor(1,0,1)
    glutSolidCube(1)
    glColor(0,0,0)
    glutWireCube(1)
    
    glutSwapBuffers()

glutInit()
glutCreateWindow("A")

glEnable(GL_DEPTH_TEST)
glClearColor(0.3, 0.5, 0.9, 1.0)
gluPerspective(75, 1, 0.1, 100)
gluLookAt(1,1,1,0,0,0,0,0,1)

glutIdleFunc(idle)
glutDisplayFunc(display)
glutMainLoop()
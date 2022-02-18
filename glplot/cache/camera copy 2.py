import numpy as np
from numpy import sin, cos
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_TIMES_ROMAN_10, GLUT_BITMAP_TIMES_ROMAN_24

class Camera:
    def __init__(self):
        self.follow = None
        self.target = np.zeros(3)
        self.euler = np.array([1.,1,0])
        self.keys = np.zeros(4, dtype=bool)
        self.distance = 6
        
        self.pan_speed = 0.2
        self.look_speed = 0.1
        self.scroll_speed = .9

    def update_view(self):
        if self.follow is not None:
            self.target = self.follow.position
            
        glLoadIdentity()
        self.direction = np.array([
            cos(self.euler[0])*cos(self.euler[1]),
            sin(self.euler[0]),
            cos(self.euler[0])*sin(self.euler[1]),
        ])
        gluLookAt(*(self.target + self.distance * self.direction), *self.target, 0,1,0)
        glutPostRedisplay()

    def onMouseDrag(self, app, m_x, m_y):
        if app.button > 0:
            dx, dy = (m_x - app.m_x) / 150, (m_y - app.m_y) / 150
            self.euler += np.array([dy, dx, 0]) * self.look_speed

    def onScroll(self, app, wheel, direction, m_x, m_y):
        self.distance -= direction * self.scroll_speed
        
    def update(self, app):
        if app.keys['w']: self.target -= self.pan_speed * np.array([cos(self.euler[1]),0,sin(self.euler[1])])
        if app.keys['a']: self.target -= self.pan_speed * np.array([sin(self.euler[1]),0,-cos(self.euler[1])])
        if app.keys['s']: self.target += self.pan_speed * np.array([cos(self.euler[1]),0,sin(self.euler[1])])
        if app.keys['d']: self.target += self.pan_speed * np.array([sin(self.euler[1]),0,-cos(self.euler[1])])
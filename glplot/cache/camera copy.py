import numpy as np
from numpy import sin, cos
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
import glm

class Camera:
    def __init__(self, app):
        self.app = app
        self.follow = None
        self.target = np.zeros(3)
        self.euler = np.array([1.,1,0])
        self.keys = np.zeros(4, dtype=bool)
        self.distance = 6
        
        self.pan_speed = 0.001
        self.look_speed = 0.01
        self.scroll_speed = .9

    def view(self):
        direction = np.array([
            cos(self.euler[0]) * cos(self.euler[1]),
            cos(self.euler[0]) * sin(self.euler[1]),
            sin(self.euler[0]),
        ])
        return glm.lookAt((self.target + self.distance * direction).tolist(), self.target.tolist(), (0,0,1)).to_list()

    def update_view(self):
        if self.follow is not None:
            self.target = self.follow.position
            
        glLoadIdentity()
        self.direction = np.array([
            cos(self.euler[0]) * cos(self.euler[1]),
            cos(self.euler[0]) * sin(self.euler[1]),
            sin(self.euler[0]),
        ])
        gluLookAt(*(self.target + self.distance * self.direction), *self.target, 0,0,1)

    def mouseMoveCallback(self, window, xpos, ypos):
        dx, dy = (xpos - self.app.xpos), (ypos - self.app.ypos)
        
        if glfwGetMouseButton(window, 2):
            if glfwGetKey(window, GLFW_KEY_LEFT_SHIFT) or glfwGetKey(window, GLFW_KEY_RIGHT_SHIFT):
                self.target -= self.pan_speed * self.distance * dy * np.array([cos(self.euler[1]),  sin(self.euler[1]), 0])
                self.target -= self.pan_speed * self.distance * dx * np.array([-sin(self.euler[1]), cos(self.euler[1]), 0])
            else:
                self.euler += np.array([dy, -dx, 0]) * self.look_speed

    def scrollCallback(self, window, xpos, ypos):
        self.distance -= ypos * self.scroll_speed
        
    def update(self, app):
        if app.keys['w']: self.target -= self.pan_speed * np.array([cos(self.euler[1]),0,sin(self.euler[1])])
        if app.keys['a']: self.target -= self.pan_speed * np.array([sin(self.euler[1]),0,-cos(self.euler[1])])
        if app.keys['s']: self.target += self.pan_speed * np.array([cos(self.euler[1]),0,sin(self.euler[1])])
        if app.keys['d']: self.target += self.pan_speed * np.array([sin(self.euler[1]),0,-cos(self.euler[1])])
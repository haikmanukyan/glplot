from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

from glplot.plot.animated_attr import AnimatedAttr

class BaseFigure:
    def __init__(self, color = [0,0,0], position = [0,0,0], rotation = [0,0,0], scale = [1,1,1]):
        self.frame_idx = 0

        self.color = AnimatedAttr(self, color)
        self.position = AnimatedAttr(self, position)
        self.rotation = AnimatedAttr(self, rotation)
        self.scale = AnimatedAttr(self, scale)

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position())
        glRotatef(self.rotation()[0], 1, 0, 0)
        glRotatef(self.rotation()[1], 0, 1, 0)
        glRotatef(self.rotation()[2], 0, 0, 1)
        glScalef(*self.scale())

        self.draw_figure()

        glPopMatrix()

    def update(self):
        self.frame_idx += 1
        self.update_figure()
    
    def draw_figure(self): pass
    def update_figure(self): pass
    
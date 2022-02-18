from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

class BaseFigure:
    def get_shape(self, arr):
        shape = []
        while hasattr(arr, '__len__'):
            shape.append(len(arr))
            arr = arr[0]
        return shape

    def animated_attr(self, attr, dims = 1):
        if callable(attr):
            return attr
        if isinstance(attr, np.ndarray):
            if len(attr.shape) == dims:
                return lambda: attr
            elif len(attr.shape) == dims + 1:
                return lambda: attr[self.frame_idx % len(attr)]
        if isinstance(attr, list) or isinstance(attr, tuple):
            shape = self.get_shape(attr)
            if len(shape) == dims:
                return lambda: attr
            elif len(shape) == dims + 1:
                return lambda: attr[self.frame_idx % len(attr)]

    def __init__(self, color = [0,0,0], position = [0,0,0], rotation = [0,0,0], scale = [1,1,1]):
        self.frame_idx = 0

        self.color = self.animated_attr(color)
        self.position = self.animated_attr(position, 1)
        self.rotation = self.animated_attr(rotation, 1)
        self.scale = self.animated_attr(scale, 1)

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
    
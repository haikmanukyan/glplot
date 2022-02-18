from OpenGL.GL import *
from OpenGL.GLU import *

from glplot.plot.base_figure import BaseFigure
import numpy as np
class Lines(BaseFigure):
    def __init__(self, X, Y, Z, **kwargs):
        super().__init__(**kwargs)
        points = np.stack([X,Y,Z], -1)
        points_arr = []
        for i in range(len(points[0]) - 1):
            points_arr.append(points[...,i,:])
            points_arr.append(points[...,i+1,:])
        points = np.stack(points_arr, 1)
        self.points = self.animated_attr(points, 2)
        self.radius = 10.0

    def draw_figure(self):
        points = self.points()
        glVertexPointer(3, GL_FLOAT, 0, points)
        glEnableClientState(GL_VERTEX_ARRAY)
        glColor3fv(self.color())
        glPointSize(self.radius)
        glDrawArrays(GL_POINTS, 0, len(points))
        glDrawArrays(GL_LINES, 0, len(points))

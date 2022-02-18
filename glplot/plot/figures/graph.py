from OpenGL.GL import *
from OpenGL.GLU import *

from glplot.plot.base_figure import BaseFigure
import numpy as np

class Graph(BaseFigure):
    def __init__(self, points, edges, **kwargs):
        super().__init__(**kwargs)

        self.points = []
        for u,v in edges:
            self.points.append(points[...,u,:])
            self.points.append(points[...,v,:])
        self.points = np.stack(self.points, -2)
        self.points = self.animated_attr(self.points, 2)

        self.radius = 5.0
        self.line_width = 2.
        self.edges = edges

    def draw_figure(self):
        points = self.points()

        glVertexPointer(3, GL_FLOAT, 0, points.flatten())
        glEnableClientState(GL_VERTEX_ARRAY)
        glColor3fv(self.color())
        glLineWidth(self.line_width)
        glPointSize(self.radius)
        glDrawArrays(GL_POINTS, 0, len(points))
        glDrawArrays(GL_LINES, 0, len(points))
        glLineWidth(1.)
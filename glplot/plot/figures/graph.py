from OpenGL.GL import *
from OpenGL.GLU import *
from glplot.plot.animated_attr import AnimatedAttr

from glplot.plot.base_figure import BaseFigure
import numpy as np

class Graph(BaseFigure):
    def __init__(self, points, edges, **kwargs):
        super().__init__(**kwargs)
        self.points = AnimatedAttr(self, points)

        self.radius = 5.0
        self.line_width = 2.
        self.edges = edges

    def get_vertices(self):
        points_arr = []
        points = self.points()
        for u,v in self.edges:
            points_arr.append(points[...,u,:])
            points_arr.append(points[...,v,:])
        return np.stack(points_arr, -2)

    def draw_figure(self):
        vertices = self.get_vertices()

        glColor3fv(self.color())
        glLineWidth(self.line_width)
        glPointSize(self.radius)
        
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, vertices.flatten())
        glDrawArrays(GL_POINTS, 0, len(vertices))
        glDrawArrays(GL_LINES, 0, len(vertices))
        
        glLineWidth(1.)
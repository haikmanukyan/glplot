from OpenGL.GL import *
from OpenGL.GLU import *

from glplot.plot.base_figure import BaseFigure
import numpy as np

class Graph(BaseFigure):
    def __init__(self, points, edges, c = [1,0,0]):
        super().__init__()
        self.points = []
        for u,v in edges:
            self.points.append(points[u])
            self.points.append(points[v])
        self.points = np.stack(self.points)

        self.radius = 5.0
        self.line_width = 2.
        self.edges = edges
        self.color = c

    def draw(self):
        glVertexPointer(3, GL_FLOAT, 0, self.points.flatten())
        glEnableClientState(GL_VERTEX_ARRAY)
        glColor3fv(self.color)
        glLineWidth(self.line_width)
        glPointSize(self.radius)
        glDrawArrays(GL_POINTS, 0, len(self.points))
        glDrawArrays(GL_LINES, 0, len(self.points))
        glLineWidth(1.)
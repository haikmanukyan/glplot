from OpenGL.GL import *
from OpenGL.GLU import *

from glplot.plot.base_figure import BaseFigure

class PointCloud(BaseFigure):
    def __init__(self, points):
        super().__init__()
        self.points = points
        self.radius = 10.0
        self.color=[1, 0, 0]

    def draw_figure(self):
        glVertexPointer(3, GL_FLOAT, 0, self.points.flatten())
        glEnableClientState(GL_VERTEX_ARRAY)
        glColor3fv(self.color)
        glPointSize(self.radius)
        glDrawArrays(GL_POINTS, 0, len(self.points))

from OpenGL.GL import *
from OpenGL.GLU import *

from glplot.plot.base_figure import BaseFigure

class PointCloud(BaseFigure):
    def __init__(self, points, **kwargs):
        super().__init__(**kwargs)
        self.points = self.animated_attr(points, 2)
        self.radius = 10.0

    def draw_figure(self):
        points = self.points()
        glVertexPointer(3, GL_FLOAT, 0, points)
        glEnableClientState(GL_VERTEX_ARRAY)
        glColor3fv(self.color())
        glPointSize(self.radius)
        glDrawArrays(GL_POINTS, 0, len(points))

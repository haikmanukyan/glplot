from OpenGL.GL import *
from OpenGL.GLU import *
from glplot.plot.animated_attr import AnimatedAttr

from glplot.plot.base_figure import BaseFigure

class PointCloud(BaseFigure):
    def __init__(self, points, **kwargs):
        super().__init__(**kwargs)
        self.points = AnimatedAttr(self, points, 2)
        self.radius = 10.0

    def draw_figure(self):
        glVertexPointer(3, GL_FLOAT, 0, self.points())
        glEnableClientState(GL_VERTEX_ARRAY)
        glColor3fv(self.color())
        glPointSize(self.radius)
        glDrawArrays(GL_POINTS, 0, len(self.points))

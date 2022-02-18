from OpenGL.GL import *
from OpenGL.GLU import *

from glplot.plot.base_figure import BaseFigure
import numpy as np
class Lines(BaseFigure):
    def __init__(self, X, Y, Z, c = [1,0,0]):
        super().__init__()
        points = np.stack([X,Y,Z], -1)
        self.points = np.stack([points[:-1],points[1:]], 1).reshape(-1,3)
        self.radius = 10.0
        self.color = c

    def draw(self):
        glVertexPointer(3, GL_FLOAT, 0, self.points.flatten())
        glEnableClientState(GL_VERTEX_ARRAY)
        glColor3fv(self.color)
        glPointSize(self.radius)
        glDrawArrays(GL_POINTS, 0, len(self.points))
        glDrawArrays(GL_LINES, 0, len(self.points))

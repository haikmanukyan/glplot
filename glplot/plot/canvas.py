from OpenGL.GL import *
from OpenGL.GLU import *

# TODO: Change to backend specific
from glfw.GLFW import *
from glplot.plot.figures.cube import Cube
from glplot.plot.figures.ground import Ground

from glplot.plot.figures.point_cloud import PointCloud

class Canvas:
    def __init__(self):
        self.figures = [Ground()]

    def draw(self):
        for figure in self.figures:
            figure.draw()
    
    def add(self, figure):
        self.figures.append(figure)

    def scatter(self, *args, **kwargs):
        self.add(PointCloud(*args, **kwargs))

    def cube(self, *args, **kwargs):
        self.add(Cube())
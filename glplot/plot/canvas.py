from OpenGL.GL import *
from OpenGL.GLU import *

# TODO: Change to backend specific
from glfw.GLFW import *
from glplot.plot.figures.cube import Cube
from glplot.plot.figures.graph import Graph
from glplot.plot.figures.ground import Ground
from glplot.plot.figures.lines import Lines

from glplot.plot.figures.point_cloud import PointCloud

class Canvas:
    def __init__(self):
        self.figures = [Ground()]

    def draw(self):
        for figure in self.figures:
            figure.draw()
    def update(self):
        for figure in self.figures:
            figure.update()
    
    def add(self, figure):
        self.figures.append(figure)

    def scatter(self, *args, **kwargs):
        self.add(PointCloud(*args, **kwargs))

    def graph(self, *args, **kwargs):
        self.add(Graph(*args, **kwargs))
    
    def plot(self, *args, **kwargs):
        self.add(Lines(*args, **kwargs))

    def cube(self, *args, **kwargs):
        self.add(Cube(*args, **kwargs))
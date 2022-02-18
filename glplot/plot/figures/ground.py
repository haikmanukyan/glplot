from OpenGL.GL import *
from OpenGL.GLU import *

from glplot.plot.base_figure import BaseFigure

class Ground(BaseFigure):
    def __init__(self):
        super().__init__()

    def draw(self):
        size = 5
        # glColor3fv([183 / 255., 180 / 255., 189 / 255.])
        glColor3fv([0.,0.,0.])

        for i in range(-size, size):
            for j in range(-size, size):
                glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )
                glBegin(GL_QUADS)                

                glVertex(i,   j  , 0.01)
                glVertex(i+1, j  , 0.01)
                glVertex(i+1, j+1, 0.01)
                glVertex(i,   j+1, 0.01)
                glEnd()
                glPolygonMode( GL_FRONT_AND_BACK, GL_FILL )

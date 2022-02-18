from OpenGL.GL import *
from OpenGL.GLU import *

from glplot.plot.base_figure import BaseFigure

vertices = (
    (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1),
    (-1, 1, 1), (-1, -1, -1), (-1, -1, 1), (-1, 1, -1)
)
edges = (
    (0, 1), (0, 3), (0, 4), (1, 2), (1, 7), (2, 5),
    (2, 3), (3, 6), (4, 6), (4, 7), (5, 6), (5, 7)
)
quads = (
    (0, 3, 6, 4), (2, 5, 6, 3), (1, 2, 5, 7),
    (1, 0, 4, 7), (7, 4, 6, 5), (2, 3, 0, 1)
)
normals = [
    ( 0,  0, -1), (-1,  0,  0), ( 0,  0,  1), 
    ( 1,  0,  0), ( 0,  1,  0), ( 0, -1,  0)
]

class Cube(BaseFigure):
    def __init__(self, c = [1,0,0]):
        super().__init__()
        self.color = c

    def draw(self):
        glColor3f(*self.color)
        glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1.))
        glMaterialfv(GL_FRONT, GL_SHININESS, 10.)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        glBegin(GL_QUADS)
        for i, surface in enumerate(quads):
            glNormal3fv(normals[i])
            for v in surface:
                glVertex3fv(vertices[v])
        glEnd()

        glLineWidth(3)
        glColor3f(0.,0.,0.)
        glBegin(GL_LINES)
        for cubeEdge in edges:
            for cubeVertex in cubeEdge:
                glVertex3fv(vertices[cubeVertex])
        glEnd()
        glLineWidth(1)
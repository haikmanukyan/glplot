import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_TIMES_ROMAN_10, GLUT_BITMAP_TIMES_ROMAN_24

cubeVertices = ((1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1),
                (-1, 1, 1), (-1, -1, -1), (-1, -1, 1), (-1, 1, -1))
cubeEdges = ((0, 1), (0, 3), (0, 4), (1, 2), (1, 7), (2, 5),
             (2, 3), (3, 6), (4, 6), (4, 7), (5, 6), (5, 7))
cubeQuads = ((0, 3, 6, 4), (2, 5, 6, 3), (1, 2, 5, 7),
             (1, 0, 4, 7), (7, 4, 6, 5), (2, 3, 0, 1))

# =================== Primitives ================
def wireCube():
    glBegin(GL_LINES)
    for cubeEdge in cubeEdges:
        for cubeVertex in cubeEdge:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()

def solidCube():
    glBegin(GL_QUADS)
    for cubeQuad in cubeQuads:
        for cubeVertex in cubeQuad:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()

# ============== Simple Shapes ================
def cube(transform):
    glPushMatrix()
    glTranslatef(*transform.position())
    rotvec = transform.rotvec()
    glRotatef(np.rad2deg(la.norm(rotvec)), *rotvec)
    glScalef(*transform.scale())

    glColor4f(1., 1., 0, 0.5)
    solidCube()
    glColor4f(1., 0., 0, 0.5)
    wireCube()
    glPopMatrix()

def draw_ground(size=5):
    glColor3fv([1.0,1.0,1.0])
    glBegin(GL_QUADS)
    glVertex(-10,0,-10)
    glVertex(-10,0, 10)
    glVertex( 10,0, 10)
    glVertex( 10,0,-10)
    glEnd()

    for i in range(-size, size):
        for j in range(-size, size):
            glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )
            glBegin(GL_QUADS)
            
            glColor3fv([183 / 255., 180 / 255., 189 / 255.])

            glVertex(i,   0.01, j  )
            glVertex(i+1, 0.01, j  )
            glVertex(i+1, 0.01, j+1)
            glVertex(i,   0.01, j+1)
            glEnd()
            glPolygonMode( GL_FRONT_AND_BACK, GL_FILL )


def sphere(x, y, z, radius, color=[1, 0, 0]):
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor4f(*color, 0.5)
    sphere = gluNewQuadric()  # Create new sphere
    gluSphere(sphere, radius, 16, 8)  # Draw sphere
    glPopMatrix()

# ================ Simple Plots ====================

def scatter(points, radius = 10.0, color=[1, 0, 0]):
    glVertexPointer(3, GL_FLOAT, 0, points.flatten())
    glEnableClientState(GL_VERTEX_ARRAY)

    glColor3fv(color)
    glPointSize(radius)
    glDrawArrays(GL_POINTS, 0, len(points))

def scatter_spheres(points, radius, color=[0, 1, 1]):
    if not hasattr(radius, '__len__'): radius = [radius] * len(points)
    glColor3fv(color)
    for point, r in zip(points, radius):
        if r == 0: continue
        sphere(*point, r * 0.1, color)

def draw_path(points, color=[1, 0, 0], size=0.05, colors=None, show_points=True):
    glLineWidth(5.0)
    glColor3fv(color)
    
    if len(points[0]) == 3:
        glBegin(GL_LINES)
        for i in range(len(points) - 1):
            glVertex3fv(points[i])
            glVertex3fv(points[i+1])
        glEnd()
        if show_points:
            if colors is None: colors = [color] * len(points)
            for point, color in zip(points, colors): sphere(*point, size, color)   
    else:
        glBegin(GL_LINES)
        for i in range(len(points) - 1):
            glVertex3f(points[i][0], 0, points[i][1])
            glVertex3f(points[i + 1][0], 0, points[i + 1][1])
        glEnd()
        if show_points:
            if colors is None: colors = [color] * len(points)
            for point, color in zip(points, colors): sphere(point[0], size, point[1], 0.1, color)

    glLineWidth(1.0)

def draw_vectors(points, vectors, color=[1, 1, 0], size=0.3):
    glLineWidth(2.0)
    glColor3f(*color)
    glBegin(GL_LINES)
    if len(points[0]) == 3:
        for i in range(len(points)):
            glVertex3fv(points[i] + [0,0.1,0])
            glVertex3fv(points[i] + size * vectors[i] + [0,0.1,0])
    else:
        for i in range(len(points)):
            glVertex3f(points[i][0], 0.1, points[i][1])
            glVertex3f(points[i][0] + size * vectors[i][0], 0.1, points[i][1] + size * vectors[i][1])
    glEnd()
    glLineWidth(1.0)

def draw_skeleton(skeleton):
    glLineWidth(3.0)
    glColor3f(*skeleton.color)
    glBegin(GL_LINES)
    for i,v in enumerate(skeleton.get_jointsnp()):
        glVertex3fv(v), glVertex3fv(skeleton.get_jointsnp()[skeleton.bones[i]])
    glEnd()
    scatter_spheres(skeleton.get_jointsnp(), 0.2, skeleton.color)
    glLineWidth(1.0)


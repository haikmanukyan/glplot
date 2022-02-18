import glplot as glp
import numpy as np

from glplot.plot.figures.graph import Graph

# points = np.random.randn(100, 100, 3)
# glp.scatter(points, color = (1.0,0.2,0))

t = 0.01 * np.arange(1000)[:,None]
X = np.cos(t) * np.arange(10)
Y = np.sin(t) * np.arange(10)
Z = X**2 + Y**2

color = np.tile(np.arange(0,1,0.001)[:,None], (1,3))
color[:,1:] = 0
print (color)
glp.plot(X, Y, Z, color = color)

# glp.cube(c = [0.8, 0.5, 0.])

skeleton_verts = np.load('build/sample.npy')
skeleton_tree = [0, 0, 1, 2, 3, 4, 0, 6, 7, 8, 9, 0, 11, 12, 13, 12, 15, 16, 17, 18, 12, 20, 21, 22, 23]
skeleton_edges = list(zip(range(len(skeleton_tree)), skeleton_tree))

# glp.graph(skeleton_verts[:100], skeleton_edges)
# rotation = np.stack([np.zeros(100), np.zeros(100), np.arange(100)], -1)
# figure = Graph(skeleton_verts, skeleton_edges, color = [1,0,0], rotation = rotation)
# glp.canvas.add(figure)

glp.show()
import glplot as glp
import numpy as np

from glplot.plot.figures.graph import Graph

class Skeleton:
    def __init__(self, path, tree):
        self.data = np.load(path)
        self.edges = list(zip(range(len(tree)), tree))
        self.frame_idx = 0

    def points(self):
        self.frame_idx += 1
        return self.data[self.frame_idx]

if __name__ == '__main__':
    # points = np.random.randn(100, 100, 3)
    # glp.scatter(points, color = (1.0,0.2,0))

    # t = 0.01 * np.arange(1000)[:,None]
    # X = np.cos(t) * np.arange(-10,10)
    # Y = np.sin(t) * np.arange(-10,10)
    # Z = 0.1 * (X**2 + Y**2)
    color = np.zeros((1000,3))
    color[:,0] = np.arange(0.0,1.0, 0.001)
    color[:,1] = np.arange(1.0,0.0,-0.001)
    # glp.plot(X, Y, Z, color = color)

    # glp.cube(c = [0.8, 0.5, 0.])

    # skeleton_verts = np.load('build/sample.npy')
    # skeleton_tree = [0, 0, 1, 2, 3, 4, 0, 6, 7, 8, 9, 0, 11, 12, 13, 12, 15, 16, 17, 18, 12, 20, 21, 22, 23]
    # skeleton_edges = list(zip(range(len(skeleton_tree)), skeleton_tree))

    skeleton = Skeleton(
        'build/sample.npy', 
        [0, 0, 1, 2, 3, 4, 0, 6, 7, 8, 9, 0, 11, 12, 13, 12, 15, 16, 17, 18, 12, 20, 21, 22, 23],
    )

    figure = Graph(skeleton.points, skeleton.edges, color = color)

    # glp.graph(skeleton_verts, skeleton_edges)
    
    rotation = np.stack([np.zeros(100), np.zeros(100), np.arange(100)], -1)
    glp.canvas.add(figure)

    p = glp.show()
    print ("Joined")
    p.join()
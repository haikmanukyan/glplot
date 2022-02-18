import glplot
import numpy as np

points = np.random.randn(100, 3)
glplot.scatter(points)

points = np.random.randn(100, 3)
glplot.scatter(points, c = (0.,0.,1.))
glplot.cube()
glplot.show()
from glplot.plot.canvas import Canvas
from glplot.glfw.app import App

canvas = Canvas()

def create_canvas():
    global canvas
    canvas = Canvas()
    return canvas

def show(): App(canvas).run()
def scatter(*args, **kwargs): canvas.scatter(*args, **kwargs)
def cube(*args, **kwargs): canvas.cube(*args, **kwargs)


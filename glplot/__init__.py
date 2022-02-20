from glplot.glfw.app import App
from glplot.plot.canvas import Canvas
from multiprocessing import Process

canvas = Canvas()

def create_canvas():
    global canvas
    canvas = Canvas()
    return canvas

def scatter(*args, **kwargs): canvas.scatter(*args, **kwargs)
def plot(*args, **kwargs): canvas.plot(*args, **kwargs)
def graph(*args, **kwargs): canvas.graph(*args, **kwargs)
def cube(*args, **kwargs): canvas.cube(*args, **kwargs)


def spawn_window(canvas):
    app = App(canvas)
    app.run()

def show(): 
    p = Process(target=spawn_window, args = (canvas,))
    p.start()
    create_canvas()
    return p
import torch
import numpy as np
from threading import Thread
from multiprocessing import Process

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_TIMES_ROMAN_10, GLUT_BITMAP_TIMES_ROMAN_24

from src.gl import gldraw
from src.gl.app import App

from src.sim.skeleton import Skeleton
from src.sim.animation import Animation
from src.sim.trajectory import Trajectory
from src.util.model_saver import ModelSaver

def _scatter(points, color=[1, 1, 1], name="Points"):
    def draw(app):
        gldraw.draw_ground()
        gldraw.scatter(points)
    App(draw = draw, name = name).run()

def _plot_skeleton(skeleton:Skeleton, color=[1, 1, 1], name="Pose"):
    def draw(app):
        gldraw.draw_ground()
        gldraw.draw_skeleton(skeleton)
    App(draw = draw, name = name).run()

def _plot_controller(controller, start_paused = True, bg_color = None, name = 'Animation'):
    app = App(draw = controller.draw, update = controller.update, bg_color = bg_color, name = name)
    app.is_paused = start_paused
    
    if hasattr(controller, 'onKeyDown'): app.onKeyDown += controller.onKeyDown
    if hasattr(controller, 'onClick'): app.onClick += controller.onClick
    if hasattr(controller, 'onMouseDrag'): app.onMouseDrag += controller.onMouseDrag
    app.run()

def _plot_pose(pose, SkeletonType, colors = None, start_paused = True, bg_color = None, name = 'Animation'):
    _plot_controller(Animation(pose, SkeletonType, colors), start_paused = start_paused, bg_color = bg_color, name = name)

def _plot_trajectory(pose, SkeletonType, name = 'Trajectory'):
    _plot_controller(Trajectory(pose, SkeletonType), name)

def _plot_model(model_path, load_source = True, name = 'Network'):
    controller = ModelSaver.load(model_path, load_source).controller
    app = App(draw = controller.draw, update = controller.update, name = name)
    
    if hasattr(controller, 'onKeyDown'): app.onKeyDown += controller.onKeyDown
    if hasattr(controller, 'onClick'): app.onClick += controller.onClick
    app.run()

def _record_pose(pose, SkeletonType, colors = None, save_path = 'data/captures/', name = 'video', overwrite = False, description = ''):
    animation = Animation(pose, SkeletonType, colors, loop = False, local=True, description = description)
    app = App(draw = animation.draw, update = animation.update, name = name)
    app.save_path = save_path
    app.overwrite = overwrite
    
    app.camera.follow = animation.skeleton
    
    app.is_paused = False
    app.start_recording()
    app.run()
def record_pose(*args, **kwargs): Process(target=_record_pose, args=args, kwargs=kwargs).start()

def _snap_pose(pose, SkeletonType, description = '', save_path = 'data/captures/', name = 'snap', colors = None, overwrite = False, n_frames = 9, dist = 0.5):
    trajectory = Trajectory(pose, SkeletonType, description = description, colors = colors, n_frames = n_frames, dist = dist)
    trajectory.snap = 0
    app = App(draw = trajectory.draw, update = trajectory.update, name = name)
    app.save_path = save_path
    app.overwrite = overwrite

    app.window_size = (1000,180)
    app.camera.euler = [0., np.pi, 0.]
    app.camera.distance = 3.0
    app.camera.target = [0.,1.,0.]
    
    app.is_paused = False
    app.run()
def snap_pose(*args, **kwargs): Process(target=_snap_pose, args=args, kwargs=kwargs).start()


def scatter(*args, **kwargs): Process(target=_scatter, args=args, kwargs=kwargs).start()
def plot_controller(*args, **kwargs): Process(target=_plot_controller, args=args, kwargs=kwargs).start()
def plot_model(*args, **kwargs): Process(target=_plot_model, args=args, kwargs=kwargs).start()
def plot_skeleton(*args, **kwargs): Process(target=_plot_skeleton, args=args, kwargs=kwargs).start()
def plot_animation(*args, **kwargs): Process(target=_plot_controller, args=args, kwargs=kwargs).start()
def plot_pose(*args, **kwargs): Process(target=_plot_pose, args=args, kwargs=kwargs).start()
def plot_trajectory(*args, **kwargs): Process(target=_plot_trajectory, args=args, kwargs=kwargs).start()

if __name__ == '__main__':
    from src.sim.skeleton import Skeleton
    from src.data.h36.vars import H36MSkeleton
    from src.data.data_loader import DataLoader
    # from src.data.nsm.nsm_dataframe_controller import NSMDataFrameController
    # from src.data.nsm.nsm_dataframe import NSMDataFrame
    # from src.data.nsm.nsm_dataset import NSMDataset

    # dataset = NSMDataset('data/nsm/clip.npy', norm = np.load('data/nsm/norm.npy').astype(np.float32), dtype = torch.float32, clip_sequences = True)
    # data = NSMDataFrame(dataset.data, dataset.norm, clips = dataset.sequences)
    # controller = NSMDataFrameController(data)
  
    # plot_controller(controller)  

    idle = DataLoader.load('data/sets/h36m-idle', read_data = True).bind()
    plot_pose(idle, H36MSkeleton, colors = [(0, 150 / 255, 255 / 255) * len(idle)], bg_color = (1.,1.,1.,1.))

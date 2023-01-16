import time
import tkinter

from models.Rect import Rect
from models.ScreenSizes import ScreenSizes
from models.Vertice import Vertice
from views import error_screen
import matplotlib.path as path
from controllers.dispersion import get_func
from controllers.integral_sum import integral_sum
from views.result_screen import *


def get_path_from_dots(dots: list[Vertice], screen_width: int):
    d = []
    for i in range(len(dots)):
        dots[i].y = screen_width - dots[i].y
        d.append([dots[i].x, dots[i].y])
    return path.Path(d), dots


def run(
    vertices: list[Vertice],
    repetitions: int,
    screen_sizes: ScreenSizes,
    root: tkinter.Tk,
):
    try:
        area, vertices_c = get_path_from_dots(vertices, screen_sizes.screen_size_width)
        f = get_func()
        rect = Rect(vertices)
        integral_sum(rect, area, repetitions, f)
        plot(rect, area, screen_sizes)
    except Exception as e:
        print(e)
        error_screen.show()
    finally:
        root.destroy()

import time
import tkinter

from controllers import function_parse
from controllers.integrals import calculate_integral
from models.Rect import Rect
from models.ScreenSizes import ScreenSizes
from models.Vertice import Vertice
from views import error_screen
import matplotlib.path as path
from controllers.dispersion import get_func
from controllers.integral_sum import integral_sum
from views.result_screen import *


def get_path_from_dots(dots, screen_width):
    d = []
    for i in range(len(dots)):
        dots[i].y = screen_width - dots[i].y
        d.append([dots[i].x, dots[i].y])
    return path.Path(d), dots


def get_vertices(vertices):
    v = []
    for i in vertices:
        v.append((i.x, i.y))
    return v


def run(
        vertices,
        repetitions,
        screen_sizes,
        root,
):
    try:
        area, vertices_c = get_path_from_dots(vertices, screen_sizes.screen_size_width)
        f = get_func()
        rect = Rect(vertices)

        new_v = get_vertices(vertices)
        new_f = function_parse.parse_function("")
        res, err = calculate_integral(new_f, new_v, repetitions)

        integral_sum(rect, area, repetitions, f, str(res), str(err))

        plot(rect, area, screen_sizes)
    except Exception as e:
        print(e)
        error_screen.show()
    finally:
        root.destroy()

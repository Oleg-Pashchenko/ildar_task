import matplotlib.pyplot as plt
import matplotlib.patches as patches

from models.Rect import Rect
from models.ScreenSizes import ScreenSizes
from models.Vertice import Vertice

fig, ax = plt.subplots()


def add_rect_to_plot(rect: Rect):
    bounds = rect.get_bounds()
    ax.add_patch(
        patches.Rectangle(
            (bounds.left_x, bounds.left_y),
            bounds.right_x - bounds.left_x,
            bounds.right_y - bounds.left_y,
            fill=False,
            edgecolor="cyan",
        )
    )


def add_legend(int_sum, disp):
    black_patch = patches.Patch(
        color="purple", label="Computed integral sum: {:.3f}".format(int_sum)
    )
    red_patch = patches.Patch(
        color="purple", label="Computed dispersion: {:.3f}".format(disp)
    )
    ax.legend(handles=[black_patch, red_patch], loc="lower left", bbox_to_anchor=(0, 1))


def add_dot_to_plot(x, y, colour="blue"):
    plt.plot(
        [x],
        [y],
        marker="o",
        markersize=1,
        markerfacecolor=colour,
        markeredgecolor=colour,
    )


def draw_plot_from_path(area_path):
    patch = patches.PathPatch(area_path, facecolor="yellow", lw=2)
    ax.add_patch(patch)
    ax.axis("scaled")
    plt.show()


def plot(rect, area_path, screen_sizes: ScreenSizes):
    global_rect = Rect(
        [
            Vertice(0, 0),
            Vertice(screen_sizes.screen_size_width, 0),
            Vertice(screen_sizes.screen_size_width, screen_sizes.screen_size_height),
            Vertice(0, screen_sizes.screen_size_height),
        ]
    )
    add_rect_to_plot(rect)
    add_rect_to_plot(global_rect)
    draw_plot_from_path(area_path)

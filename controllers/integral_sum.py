from views import error_screen
from views.result_screen import *
from controllers.dispersion import *


def is_dot_inside(area, dot):
    return area.contains_point(dot)


def integral_sum(rect: Rect, area, n, f, t1, t2):
    n = int(n)
    bounds = rect.get_bounds()
    width, height = bounds.right_x - bounds.left_x, bounds.right_y - bounds.left_y

    x_space = width / (2 * n)
    y_space = height / (2 * n)

    high_point = [bounds.left_x, bounds.right_y]
    computed_res = 0
    area_sq = x_space * y_space * 4

    for i in range(n):
        for j in range(n):
            x_offset = high_point[0] + x_space * (1 + 2 * i)
            y_offset = high_point[1] - y_space * (1 + 2 * j)

            if is_dot_inside(area, (x_offset, y_offset)):
                computed_res += f(x_offset, y_offset)
                add_diff_dot(x_offset, y_offset)
                add_dot_to_plot(x_offset, y_offset, "purple")
            else:
                add_dot_to_plot(x_offset, y_offset)

    # if integral_s == 0:
    #    error_screen.show()
    add_legend(t1, t2)

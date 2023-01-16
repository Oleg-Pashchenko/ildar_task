import sympy

x = sympy.Symbol("x")
y = sympy.Symbol("y")
f = x * sympy.ln(y)
diff_const = 6 / 24
gl_sum = 0


def f_eval(_x, _y):
    return f.evalf(subs={x: _x, y: _y})


def get_func():
    return f_eval


def get_derivative():
    df_ddx = sympy.diff(f, x, 2)
    df_ddy = sympy.diff(f, y, 2)
    return df_ddx, df_ddy


def add_diff_dot(_x, _y):
    global gl_sum
    dx, dy = get_derivative()
    disp_value = dx.evalf(subs={x: _x, y: _y}) + dy.evalf(subs={x: _x, y: _y})
    gl_sum += disp_value


def get_dispersion(s, h):
    global gl_sum, diff_const
    return diff_const * s * (h**2) * gl_sum

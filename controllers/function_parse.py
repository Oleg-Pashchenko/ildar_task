def is_function_text_correct(function_text):
    available = [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
        "+", "-", "*", "/", "^", "(", ")", "x", "y", "sin", "cos", "tan", "asin", "acos", "atan"
    ]

    for symbol in available:
        function_text = function_text.replace(symbol, "")

    return not bool(function_text)


def parse_function(function_text):
    if not is_function_text_correct(function_text):
        return None

    try:
        function_text = "lambda x, y: " + function_text
        function_text = function_text.replace("^", "**")
        fun = eval(function_text)

        try:
            fun(0, 0)
        except SyntaxError:
            return None
        except NameError:
            return None
        except Exception:
            pass
        return fun
    except Exception as e:
        return None

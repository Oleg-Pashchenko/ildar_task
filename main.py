from models.ScreenSizes import ScreenSizes
from views.start_screen import StartScreen
import json


def read_config() -> dict:
    try:
        return json.loads(open(file="config.json", mode="r", encoding="UTF-8").read())

    except Exception:
        print("Ошибка чтения Json! Проверьте, существует ли файл!")
        exit(1)


def read_screen_sizes() -> ScreenSizes:
    config = read_config()
    try:
        return ScreenSizes(
            screen_size_width=config["screen_size"]["width"],
            screen_size_height=config["screen_size"]["height"],
            error_message_size_width=config["error_message_size"]["width"],
            error_message_size_height=config["error_message_size"]["height"],
        )
    except Exception:
        print("Параметры не найдены или не валидны!\nУстановлены дефолтные!")
        return ScreenSizes(
            screen_size_width=800,
            screen_size_height=600,
            error_message_size_width=400,
            error_message_size_height=200,
        )


def main():
    screen_sizes = read_screen_sizes()
    screen = StartScreen(screen_sizes)
    screen.launch()


if __name__ == "__main__":
    main()

import threading
import time
import tkinter as tk

from controllers import calculations
from models.ScreenSizes import ScreenSizes
from models.Vertice import Vertice


class StartScreen:
    vertices = []
    start_x, start_y, canvas, root, repetitions = None, None, None, None, 1

    def __init__(self, screen_sizes: ScreenSizes):
        self.screen_sizes = screen_sizes

    def save_vertices(self, event):
        """Обработка нажатия на canvas"""
        if not self.start_x and not self.start_y:  # если точка стартовая
            self.start_x, self.start_y = event.x, event.y
        else:  # иначе соединяем текущую точку с предыдущей
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y)
            self.start_x, self.start_y = event.x, event.y
        self.vertices.append(Vertice(x=event.x, y=event.y))  # сохраняем текущую точку

    def on_select(self, v):
        """Запись движения ползунка"""
        self.repetitions = v

    def run(self):
        """Запуск расчета"""
        if len(self.vertices) > 2:  # дорисовываем фигуру
            self.canvas.create_line(
                self.vertices[-1].x,
                self.vertices[-1].y,
                self.vertices[0].x,
                self.vertices[0].y,
            )
            self.vertices.append(
                Vertice(x=self.vertices[0].x, y=self.vertices[0].y)
            )  # сохраняем текущую точку
        self.root.update()
        calculations.run(self.vertices, self.repetitions, self.screen_sizes, self.root)

    def launch(self):
        """Отрисовка экрана"""
        self.root = tk.Tk()
        self.root.title("Rusile | Math-lab-1")
        self.root.config(cursor="pencil")
        self.root.geometry(
            f"{self.screen_sizes.screen_size_width}x{self.screen_sizes.screen_size_height}"
        )
        self.canvas = tk.Canvas(self.root, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        scale = tk.Scale(
            self.root, from_=1, to=100, orient="horizontal", command=self.on_select
        )
        scale.pack()

        run_button = tk.Button(self.root, text="Run", command=self.run)
        run_button.pack()

        self.canvas.bind("<Button-1>", self.save_vertices)
        self.canvas.bind("<B1-Motion>", self.save_vertices)

        self.root.mainloop()

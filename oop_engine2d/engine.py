import queue
import threading
from typing import Literal
from colorama import init as colorama_init
from colorama import Fore
from tkinter import *
from oop_engine2d.figures import *

colorama_init()


def generate_start_point():
    x = random.randrange(50, 725)
    y = random.randrange(125, 550)
    return x, y


class Engine2D:

    def __init__(self):
        self.buttons = []
        self.current_color = self.colors[0]
        self.draw_queue = queue.Queue()
        self.canvas_width = 800
        self.canvas_height = 600
        self.canvas = Canvas(bg='#C0C0C0', height=self.canvas_height, width=self.canvas_width)

    def init_app(self):
        self.init_buttons()
        self.init_canvas()

    def init_buttons(self):
        font = 'sans 13 bold'
        bg = '#A9A9A9'
        width='10'
        button_triangle = Button(bg=bg, font=font, name='figure_triangle', width=width, text='Triangle',
                                 command=self.button_add_triangle)
        button_rectangle = Button(bg=bg, font=font, name='figure_rectangle', width=width, text='Rectangle',
                                  command=self.button_add_rectangle)
        button_circle = Button(bg=bg, font=font, name='figure_circle', width=width, text='Circle',
                               command=self.button_add_circle)
        button_recolor = Button(name='recolor', width=width, text='Recolor', command=self.button_recolor)
        button_draw = Button(name='draw', width=width, text='Draw', command=self.button_draw)

        self.buttons = [button_triangle, button_rectangle, button_circle, button_recolor, button_draw]

        spacing = 130
        start_x = (self.canvas_width / 2) - (len(self.buttons) + (len(self.buttons) - 1) * spacing) / 2
        for i in range(len(self.buttons)):
            x = start_x + i * spacing
            self.buttons[i].config(fg=self.current_color[0])
            self.buttons[i].place(x=x, y=20)

    def init_canvas(self):
        self.canvas.pack()
        mainloop()

    def write_figure_name(self, figure_name):
        height = self.canvas.winfo_height() - 20 * (self.draw_queue.qsize() + 1)
        self.canvas.create_text(50, height, text=figure_name, fill=self.current_color[0])

    def button_add_triangle(self):
        triangle = Triangle(self.canvas, self.current_color, generate_start_point())
        self.write_figure_name('Triangle')
        self.draw_queue.put(triangle)

    def button_add_rectangle(self):
        rectangle = Rectangle(self.canvas, self.current_color, generate_start_point())
        self.write_figure_name('Rectangle')
        self.draw_queue.put(rectangle)

    def button_add_circle(self):
        circle = Circle(self.canvas, self.current_color, generate_start_point())
        self.write_figure_name('Circle')
        self.draw_queue.put(circle)

    def button_draw(self):
        self.clear_canvas()
        self.set_buttons_state('disabled')
        while not self.draw_queue.empty():
            figure = self.draw_queue.get()
            figure.draw()
        threading.Timer(5, self.clear_canvas).start()
        threading.Timer(5, lambda: self.set_buttons_state('active')).start()

    def set_buttons_state(self, state: Literal['active', 'disabled']):
        for i in range(len(self.buttons)):
            self.buttons[i].config(state=state)

    def clear_canvas(self):
        self.canvas.delete('all')

    colors = [('black', Fore.BLACK),
              ('red', Fore.RED),
              ('green', Fore.GREEN),
              ('blue', Fore.BLUE),
              ('yellow', Fore.YELLOW),
              ('white', Fore.WHITE),
              ('cyan', Fore.CYAN)]

    def button_recolor(self, color=None):
        self.current_color = color if color is not None \
            else self.colors[random.randrange(len(self.colors))]
        for i in range(len(self.buttons)):
            if 'figure_' in self.buttons[i].winfo_name():
                self.buttons[i].config(fg=self.current_color[0])

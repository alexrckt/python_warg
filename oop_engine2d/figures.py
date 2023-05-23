import random
from abc import ABC, abstractmethod
from tkinter import Canvas


class Figure(ABC):

    def __init__(self, color, canvas: Canvas, start_point):
        self.color = color
        self.canvas = canvas
        self.start_point = start_point

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def print(self):
        pass


class Triangle(Figure):

    def __init__(self, canvas, color, start_point):
        super().__init__(color, canvas, start_point)
        self.height = random.randrange(50, 150)

    def draw(self):
        x = self.start_point[0]
        y = self.start_point[1]
        points = [x, y, x-self.height/2, y+self.height, x+self.height/2, y+self.height]
        self.canvas.create_polygon(points, fill=self.color[0])
        self.print()

    def print(self):
        print(self.color[1] + 'Drawing Triangle with starting point: '
              + str(self.start_point) + ' and height: ' + str(self.height))


class Rectangle(Figure):

    def __init__(self, canvas, color, start_point):
        super().__init__(color, canvas, start_point)
        self.side_length = random.randrange(50, 150)

    def draw(self):
        x = self.start_point[0]
        y = self.start_point[1]
        points = (x, y, x+self.side_length, y+self.side_length)
        self.canvas.create_rectangle(points, fill=self.color[0])
        self.print()

    def print(self):
        print(self.color[1] + 'Drawing Rectangle with starting point: '
              + str(self.start_point) + ' and side length: ' + str(self.side_length))


class Circle(Figure):

    def __init__(self, canvas, color, start_point):
        super().__init__(color, canvas, start_point)
        self.diameter = random.randrange(50, 150)

    def draw(self):
        x = self.start_point[0]
        y = self.start_point[1]
        points = (x, y, x+self.diameter, y+self.diameter)
        self.canvas.create_oval(points, fill=self.color[0])
        self.print()

    def print(self):
        print(self.color[1] + 'Drawing Circle with starting point: '
              + str(self.start_point) + ' and diameter: ' + str(self.diameter))
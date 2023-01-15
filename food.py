from turtle import Turtle
from random import choice
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Food(Turtle):
    def __init__(self, scale):
        super().__init__()
        self.food_position = []
        self.food_ob_list = []
        self.scale = scale
        self.size = 0.15 * scale
        self.hideturtle()
        self.speed('fastest')
        self.shape('turtle')
        self.penup()
        self.shapesize(self.size)
        self.color('#445526')
        self.refresh()

    def refresh(self):
        x = choice(list(range(-30 * self.scale - 5 * self.scale, 30 * self.scale + 5 * self.scale + 1, MOVE_DISTANCE)))
        y = choice(list(range(-15 * self.scale - 5 * self.scale, 15 * self.scale + 5 * self.scale + 1, MOVE_DISTANCE)))
        # print(list(range(-30 * self.scale - 5 * self.scale, 30 * self.scale + 5 * self.scale + 1, MOVE_DISTANCE)))
        # print(list(range(-15 * self.scale - 5 * self.scale, 15 * self.scale + 5 * self.scale + 1, MOVE_DISTANCE)))
        self.setpos(x, y)
        self.showturtle()
        self.food_position.append(self.pos())
        # print(self.pos())



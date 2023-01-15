from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.shapesize(8, 8)
        self.speed('fastest')
        self.color('#2f3e07')
        self.penup()

class Text(Turtle):
    def __init__(self, skl):
        super().__init__()
        self.speed('fastest')
        self.hideturtle()
        self.penup()
        self.scale = skl
    def gameover(self):
        self.setpos(0, 0)
        self.write(arg='Game Over', align='center', font=('Arial', 4 * self.scale, 'bold'))
    def scoreboard(self, scr_n):
        self.clear()
        self.setpos(0, 25 * self.scale + 4 * self.scale)
        self.write(f'Score: {scr_n}', align='center', font=('Arial', 4 * self.scale, 'bold'))






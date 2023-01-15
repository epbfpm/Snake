from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, scale):
        self.size = 0.2 * scale
        self.segments = []
        self.segment_positions = []
        self.create_snake()
        self.head = self.segments[0]
        self.head_position = self.segment_positions[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shapesize(self.size)
        new_segment.shape('square')
        new_segment.color('#445526')
        new_segment.speed('fastest')
        new_segment.penup()
        self.segments.append(new_segment)
        new_segment.setpos(position)
        self.segment_positions.append(new_segment.pos())

    def move(self):
        for seg in range(0, len(self.segments)):
            if seg == 0:
                pos = self.segments[seg].pos()
                self.segments[seg].forward(MOVE_DISTANCE)
            else:
                pos2 = self.segments[seg].pos()
                self.segments[seg].setpos(pos)
                pos = pos2
            self.segment_positions[seg] = pos
        # print(f'head {self.head.pos()}')
    def w(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def s(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def a(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def d(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)






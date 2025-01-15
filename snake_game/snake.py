
from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.position_initial_snake()
        self.head = self.segments[0]

    def position_initial_snake(self):
        for position in self.starting_position:
            self.add_segment(position)

    def move_forward(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def add_segment(self, position):
        block = Turtle("square")
        block.color("white")
        block.penup()
        block.goto(position)
        self.segments.append(block)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
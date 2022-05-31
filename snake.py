from turtle import Turtle


class Snake:
    def __init__(self):
        self.body = []
        for segment in [(0, 0), (-20, 0), (-40, 0)]:
            self.add_segment(segment)

    def add_segment(self, position):
        segment = Turtle('square')
        segment.penup()
        segment.goto(position)
        self.body.append(segment)

    def extend(self):
        self.add_segment(position=self.body[-1].position())

    def move(self):
        for seg_num in range((len(self.body) - 1), 0, -1):
            self.body[seg_num].goto(self.body[seg_num - 1].pos())
        self.body[0].forward(20)

    def up(self):
        if self.body[0].heading() != 270:
            self.body[0].seth(90)

    def down(self):
        if self.body[0].heading() != 90:
            self.body[0].seth(270)

    def left(self):
        if self.body[0].heading() != 0:
            self.body[0].seth(180)

    def right(self):
        if self.body[0].heading() != 180:
            self.body[0].seth(0)

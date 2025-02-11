from turtle import Turtle
SNAKE_LENGTH = 3
MOVE_DISTANCE = 20
START_X = 0
START_Y = 0
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.start_x = START_X
        self.start_y = START_Y
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(SNAKE_LENGTH):
            self.add_segment(self.start_x, self.start_y)
            self.start_x -= 20

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if int(self.head.heading()) != DOWN:
            self.head.seth(UP)

    def down(self):
        if int(self.head.heading()) != UP:
            self.head.seth(DOWN)

    def left(self):
        if int(self.head.heading()) != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if int(self.head.heading()) != LEFT:
            self.head.seth(RIGHT)

    def add_segment(self, x, y):
        segment = Turtle("square")
        segment.color("white")
        segment.pu()
        segment.teleport(x,y)
        self.segments.append(segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.start_x = START_X
        self.start_y = START_Y
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        x = self.segments[-1].xcor()
        y = self.segments[-1].ycor()
        self.add_segment(x,y)




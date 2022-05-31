from turtle import Turtle


class Paddle:
    def __init__(self, x_cor, y_coor):
        self.x_coor = x_cor
        self.y_coor = y_coor
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(self.x_coor, self.y_coor)
        self.paddle.shapesize(5, 1)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_x = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_x)










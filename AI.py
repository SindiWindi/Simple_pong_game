import turtle

class Ai:
    def __init__(self, x, y):
        self.x = x
        self.y = y


        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape('square')
        self.paddle.color('white')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, y)
        self.paddle.color('DarkOrchid1')

    def paddle_up(self):
        y = self.paddle.ycor()
        y += 5
        self.paddle.sety(y)
                                     ##  same methods as in player paddle class, but with lowered speed to make it look smooth
    def paddle_down(self):
        y = self.paddle.ycor()
        y -= 5
        self.paddle.sety(y)





import turtle

class Paddle:
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
        self.paddle.color('SlateBlue1')

    def paddle_up(self):
        y = self.paddle.ycor()
        y += 50
        self.paddle.sety(y)

    def paddle_down(self):
        y = self.paddle.ycor()
        y -= 50
        self.paddle.sety(y)




# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto((0, 0))
ball.dx = 0.3
ball.dy = 0.3
ball.color('LightSkyBlue1')

#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


class Menu:
    def __init__(self, col, siz):

        tlt = turtle.Turtle()
        tlt.penup()
        tlt.speed(0)
        tlt.hideturtle()
        tlt.goto(0, 200)
        tlt.color(col)
        tlt.write("P o n g", align='center', font=('Comic Sans', siz, 'bold'))

class Button:
    def __init__(self, x, y):


        self.button = turtle.Turtle()
        self.button.speed(0)
        self.button.penup()
        self.button.goto(0, y)
        self.button.shape(x)





    ## drawing button










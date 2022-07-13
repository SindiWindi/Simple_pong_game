import turtle
from Func import Paddle, ball, pen
from AI import Ai

wn = turtle.Screen()
wn.title("Pong by Sindi")
wn.bgpic('images/nice 1.gif')

wn.setup(width=800, height=600)
wn.tracer(0)

# Paddles

paddle_a = Paddle(-350, 0)
paddle_b = Ai(350, 0)




wn.listen()
wn.onkeypress(paddle_a.paddle_up, 'w')
wn.onkeypress(paddle_a.paddle_down, 's')



# Score
score_a = 0
score_b = 0

pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, 'normal'))


while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, 'normal'))

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.paddle.ycor() + 40 and ball.ycor() > paddle_b.paddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.paddle.ycor() + 40 and ball.ycor() > paddle_a.paddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1



    #AI

    if paddle_b.paddle.ycor() < ball.ycor() and abs(paddle_b.paddle.ycor() - ball.ycor()) > 40:
        paddle_b.paddle_up()

    elif paddle_b.paddle.ycor() > ball.ycor() and abs(paddle_b.paddle.ycor() - ball.ycor()) > 40:
        paddle_b.paddle_down()


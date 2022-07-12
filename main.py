from subprocess import call
import turtle
from Func import ball, pen, Menu
from AI import Ai
import tkinter as tk


wn = turtle.Screen()
wn.title("Pong by Sindi")
wn.bgpic('nice 1.gif')

wn.setup(width=800, height=600)
wn.tracer(0)

# Paddles

paddle_a = Ai(-350, 0)
paddle_b = Ai(350, 0)



tlt1 = Menu('DarkOrchid4', 42)
tlt2 = Menu('DarkOrchid', 40)


def test1():
    call(['python', 'PVP.py'])


def test2():
    call(['python', 'PVE.py'])

canvas = turtle.getcanvas()
parent = canvas.master

click_btn1 = tk.PhotoImage(file='pvp_button.gif')
click_btn2 = tk.PhotoImage(file='vs_ai.gif')

button1 = tk.Button(parent, image=(click_btn1), padx=70, pady=30, command=test1)
id1 = canvas.create_window((0, 100), window=button1)

button2 = tk.Button(parent, image=(click_btn2), padx=70, pady=30, command=test2)
id2 = canvas.create_window((0, -100), window=button2)







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
        pen.clear()


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

        pen.clear()


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

    if paddle_a.paddle.ycor() < ball.ycor() and abs(paddle_a.paddle.ycor() - ball.ycor()) > 40:
        paddle_a.paddle_up()

    elif paddle_a.paddle.ycor() > ball.ycor() and abs(paddle_a.paddle.ycor() - ball.ycor()) > 40:
        paddle_a.paddle_down()

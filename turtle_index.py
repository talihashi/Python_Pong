import turtle

#screen
turtle.setup(400, 300)
turtle.bgcolor("black")

#paddle1
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color("red")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.dy = 0

#paddle2
paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.color("red")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)
paddle2.dy = 0

#ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("teal")
ball.penup()
ball.goto(0, 0)

#Rules
game_over = False
winner = None
points = {
    "player1": 0,
    "player2": 0
}
game_rules = {
    "max_points": 3,
    "ball_speed": 3
}

#score
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0 Player 2: 0", align = "center", font = ("Arial", 24, "normal"))

paddle1.sety(paddle1.ycor() + paddle1.dy)
paddle2.sety(paddle2.ycor() + paddle2.dy)
ball.setx(ball.xcor() + ball.dx)
ball.sety(ball.ycor() + ball.dy)

#Game over
if points["player1"] == game_rules["max_points"]:
    game_over = True
    winner = "player1"
elif points["player2"] == game_rules["max_points"]:
    game_over = True
    winner = "player2"

#paddle collision
if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
    ball.setx(340)
    ball.dx *= -1
elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
    ball.setx(-340)
    ball.dx *= -1

#offscreen
if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
    points["player1"] += 1
elif ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
    points["player2"] += 1

#top or bottom collision
if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1
elif ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

#score update after conditions
score_display.clear()
score_display.write(f"Player 1: {'player1'} Player 2: {'player2'}", align="center", font=("Arial", 24, "normal"))

#paddle movement
def paddle1_up():
    paddle1.dy = 10

def paddle1_down():
    paddle1.dy = -10

def paddle2_up():
    paddle2.dy = 10

def paddle2_down():
    paddle2.dy = -10

#key bindings
turtle.listen()
turtle.onkeypress(paddle1_up, "w")
turtle.onkeypress(paddle1_down, "s")
turtle.onkeypress(paddle2_up, "Up")
turtle.onkeypress(paddle2_down, "Down")

#Game over
game_over_display = turtle.Turtle()
game_over_display.color("white")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)
game_over_display.write(f"Game over! {'winner'} wins!", align="center", font=("Arial", 36, "normal"))
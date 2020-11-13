#-----import turtle-----

import turtle as trtl
import random
import time

#-----game configuration-----

current_score = 0
high_score = 0
delay = 0.1

#-----initialize turtle-----

setup = trtl.Screen()
setup.title("Snake")
setup.bgcolor('pale green')
setup.setup(width=650, height=660)
setup.tracer(0)

top = trtl.Turtle()
top.speed(0)
top.shape("square")
top.color("dim gray")
top.penup()
top.goto(0, 0)
top.direction = "stop"

blocks= trtl.Turtle()
blocks.speed(0)
blocks.shape("square")
blocks.color("black")
blocks.penup()
blocks.goto(0, 100)

title = trtl.Turtle()
title.speed(0)
title.color("black")
title.penup()
title.ht()
title.goto(0, 293)
title.write("Snake", align = "center", font=("digital-7", 24, "normal"))

scoreboard_highscore = trtl.Turtle()
scoreboard_highscore.speed(0)
scoreboard_highscore.shape("square")
scoreboard_highscore.color("black")
scoreboard_highscore.penup()
scoreboard_highscore.ht()
scoreboard_highscore.goto(311, 293)
scoreboard_highscore.write("High Score: 0", align = "right", font=("digital-7", 24, "normal"))

scoreboard_score = trtl.Turtle()
scoreboard_score.speed(0)
scoreboard_score.shape("square")
scoreboard_score.color("black")
scoreboard_score.penup()
scoreboard_score.ht()
scoreboard_score.goto(-310, 293)
scoreboard_score.write("Score: 0", align = "left", font=("digital-7", 24, "normal"))

border = trtl.Turtle()
border.speed(0)
border.penup()
border.goto(-310, 291)
border.pendown()
border.width(2)
border.forward(622)
border.right(90)
border.forward(603)
border.right(90)
border.forward(623)
border.right(90)
border.forward(603)
border.right(90)
border.forward(10)
border.right(180)
border.forward(11)
border.ht()

trails = []

#-----game functions-----

def go_up():
    if top.direction != "down":
        top.direction = "up"

def go_down():
    if top.direction != "up":
        top.direction = "down"

def go_left():
    if top.direction != "right":
        top.direction = "left"

def go_right():
    if top.direction != "left":
        top.direction = "right"

def move():
    if top.direction == "up":
        y = top.ycor()
        top.sety(y+20)
    if top.direction == "down":
        y = top.ycor()
        top.sety(y-20)
    if top.direction == "left":
        x = top.xcor()
        top.setx(x-20)
    if top.direction == "right":
        x = top.xcor()
        top.setx(x+20)

#-----events-----

setup.listen()
setup.onkeypress(go_up, "Up")
setup.onkeypress(go_down, "Down")
setup.onkeypress(go_left, "Left")
setup.onkeypress(go_right, "Right")

while True:
    setup.update()

    if top.xcor()>290 or top.xcor()<-290 or top.ycor()>260 or top.ycor()<-290:
        time.sleep(1)
        top.goto(0, 0)
        top.direction = "stop"

        for trail in trails:
            trail.goto(1000, 1000)
        trails.clear()

        current_score = 0000

        delay = 0.1

        scoreboard_score.clear()
        scoreboard_score.write("Score: {}".format(current_score), align="left", font=("digital-7", 24, "normal"))

        scoreboard_highscore.clear()
        scoreboard_highscore.write("High Score: {}".format(high_score), align="right", font=("digital-7", 24, "normal"))

    if top.distance(blocks) <20:
        x = random.randint(-290, 270)
        y = random.randint(-290, 270)
        blocks.goto(x, y)

        new_trail = trtl.Turtle()
        new_trail.speed(0)
        new_trail.shape("square")
        new_trail.color("gray")
        new_trail.penup()
        trails.append(new_trail)

        delay -= 0.001
        current_score += 10

        if current_score > high_score:
            high_score = current_score
        scoreboard_score.clear()
        scoreboard_score.write("Score: {}".format(current_score), align="left", font=("digital-7", 24, "normal"))

        scoreboard_highscore.clear()
        scoreboard_highscore.write("High Score: {}".format(high_score), align="right", font=("digital-7", 24, "normal"))

    for index in range(len(trails)-1, 0, -1):
        x = trails[index-1].xcor()
        y = trails[index-1].ycor()
        trails[index].goto(x, y)
    if len(trails)>0:
        x = top.xcor()
        y = top.ycor()
        trails[0].goto(x, y)

    move()

    for trail in trails:
        if trail.distance(top)<20:
            time.sleep(1)
            top.goto(0, 0)
            top.direction = "stop"

            for trail in trails:
                trail.goto(1000, 1000)
            trails.clear()
            current_score = 0000
            delay = 0.1
    
            scoreboard_score.clear()
            scoreboard_score.write("Score: {}".format(current_score), align="left", font=("digital-7", 24, "normal"))

            scoreboard_highscore.clear()
            scoreboard_highscore.write("High Score: {}".format(high_score), align="right", font=("digital-7", 24, "normal"))
    time.sleep(delay)
setup.mainloop()

setup.done()
#Snake Game

#Module Header

import os
import turtle as tur
import time
import random

#Time Delay

delay = 0.08

#Screen Initalized

wn = tur.Screen()
wn.title("Snake game by @Steve")
wn.bgcolor("red")
wn.setup(width = 700, height =700)
wn.tracer(0) #Turn off the screen updates

#Object Create

head = tur.Turtle() #Head

'''
head.begin_fill()
head.fillcolor("orange")
head.color("white")
head.circle(30, steps = 4)
head.end_fill()
'''
head.speed(0)
head.shape("triangle")
head.color("white")
head.penup()
head.setheading(90)
head.goto(0, 0)
head.direction = "stop"


food = tur.Turtle() #Food
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0, 150)
food.direction = "stop"

segments = [] #Body

pen = tur.Turtle() #Score
pen.speed(1)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Score: 0 High Score: 0", align= "center", font= ("Courier", 22, "normal"))
score = 0
high_score = 0


#Function

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 15)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 15)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 15)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 15)

def go_up():
    if head.direction != "down":
        head.direction = "up"
        head.setheading(90)
def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.setheading(270)
def go_left():
    if head.direction != "right":
        head.direction = "left"
        head.setheading(180)
def go_right():
    if head.direction != "left":
        head.direction = "right"
        head.setheading(0)
        
#Exit the game

def exited():
    score = 5
    wn.bye()
    
#Press Receiving
        
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(exited, "q")

#Main Loop

while True:
    
    wn.update()

    #Eat the food
    
    if head.distance(food) <  20:
        x = random.randint(-345, 340)
        y= random.randint(-345, 345)
        food.goto(x, y)
        new_segment = tur.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        
        segments.append(new_segment)

        delay -= 0.0012

        pen.clear()
        
        #Score++
        
        score += 10
        if score > high_score:
            high_score = score
            pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font= ("Courier", 22, "normal"))

    #Add to the body

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    #Check the collision to the border
    
    if head.xcor() > 346 or head.xcor() < -346 or head.ycor() > 346 or head.ycor() < -346:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        head.setheading(90)
        
        delay = 0.08
        
        for segment in segments:
            segment.goto(1100, 1100)
        segments.clear()
        score = 0
        pen.clear()
        pen.write("You Dead.", align = "center", font = ("Arial", 25, "normal") )
        time.sleep(0.6)
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font= ("Courier", 22, "normal"))

    #Check for the head collision with the body
        
    for segment in segments:
        if segment.distance(head) < 15:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            head.setheading(90)
            
            delay = 0.08

            for segment in segments:
                segment.goto(1100, 1100)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("You Dead.", align = "center", font = ("Arial", 25, "normal") )
            time.sleep(0.6)
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font= ("Courier", 22, "normal"))
            
    #Winning Condition

    if score > 1200:
        time.sleep(0.5)
        wn.bye()
        print("You win, Baby!")
        break


   
    
    time.sleep(delay)
wn.mainloop

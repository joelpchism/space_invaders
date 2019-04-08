import turtle
import os
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15



enemyspeed = 2

#choose a number of enemies
number_of_enemies = 5
#create an empty list of enemies
enemises = []

#add enemise to a list
for i in range(number_of_enemies):
    # create then enemy
    enemises.append(turtle.Turtle())

for enemy in enemies: 
    enemy = turtle.Turtle()
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

# player's gun!
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0.5)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# define bullet state
# ready - ready to fire
# fire -bullet is firing
bulletstate = "ready"

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -200:
        x = - 280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x) 

def fire_bullet():
    # declare bulletstate as a gobal if it needs to be changed
    global bulletstate 
    if bulletstate == "ready":
        bulletstate = "fire"    
        # move the bullet to the just above a player 
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# key bind stuff ooh yah!
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

while True:
    
    for enemy in enemies:
        # move da enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        
        #move enemy back and down 
        if enemy.xcor() > 280:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)
        
        if enemy.xcor() < -280:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)

    # move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check if the bullet has gone to the top
    if bullet.ycor() > 275:
         bullet.hideturtle()
         bulletstate = "ready"

    # check for a collision betwen the bullet and the enemy
    if isCollision(bullet, enemy):
        # restart the bullet
        bullet.hideturtle
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # reset the enemy
        enemy.setposition(-200, 250)

    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hidturtle()
        print ("Game Over")
        break





delay = input("press enter to exit")
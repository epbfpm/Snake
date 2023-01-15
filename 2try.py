from turtle import Turtle, Screen
from random import choice
from time import sleep

game_is_on = True
screen = Screen()
screen.colormode(255)
screen.screensize(canvwidth=840, canvheight=640, bg='#a4be3d')
screen.listen()
print(screen.screensize())

snake_head = Turtle()
snake_head.hideturtle()
snake_head.speed('fastest')
snake_head.shape('square')
snake_head.color('#445526')
snake_head.penup()
snake_head.shapesize(1.6, 1.6)
snake_head.setpos(-380, 280)
snake_head.showturtle()

stamp_ids = []
snake_segments = [(-380, 280)]
new_food_position =[]
number_snake_segments = 3
speed = 0.3
if number_snake_segments % 3 == 0 and number_snake_segments < 100:
    speed -= 0.03

score = Turtle()
score.hideturtle()
score.penup()
score.setpos(0, 350)

border = Turtle()
border.hideturtle()
border.shape('square')
border.shapesize(8, 8)
border.speed('fastest')
border.color('#2f3e07')
border.penup()
border.setposition(-420, 320)
border.pendown()
border.setposition(-420, -320)
border.setposition(420, -320)
border.setposition(420, 320)
border.setposition(-420, 320)

food = Turtle()
food.hideturtle()
food.speed('fastest')
food.shape('turtle')
food.penup()
food.shapesize(1.2)
food.color('#445526')
food.setpos(-100, 40)
food.showturtle()
apple_position = [-100, 40]


def eat():
    global number_snake_segments
    cleo = True
    while food.pos() in snake_segments or cleo:
        x = choice(list(range(-380, 384, 40)))
        y = choice(list(range(-280, 284, 40)))
        food.setpos(x, y)
        print(food.pos())
        print(snake_segments)
        print((x, y) in snake_segments)
        cleo = False
    number_snake_segments += 1
    score.clear()
    score.write(f'Score: {number_snake_segments - 3}', align='center', font=('Arial', 20, 'bold'))

def snake_length():
    stamp_ids.append(snake_head.stamp())
    snake_segments.append(snake_head.position())
    if len(stamp_ids) + 1 > number_snake_segments:
        snake_head.clearstamp(stamp_ids[0])
        stamp_ids.remove(stamp_ids[0])
        snake_segments.remove(snake_segments[0])
def end():
    global game_is_on
    lose = Turtle()
    lose.hideturtle()
    lose.penup()
    lose.write(arg='GAME OVER!', align='center', font=('Arial', 20, 'bold'))
    game_is_on = False

def collision():
    if snake_head.position() in snake_segments:
        end()
    elif snake_head.xcor() > 380 or \
            snake_head.ycor() > 280 or \
            snake_head.xcor() < -380 or \
            snake_head.ycor() < -280:
        end()
    elif snake_head.xcor() == food.xcor() and snake_head.ycor() == food.ycor():
        eat()

def w():
    if snake_head.heading() != 270:
        snake_head.setheading(90)
def s():
    if snake_head.heading() != 90:
        snake_head.setheading(270)
def a():
    if snake_head.heading() != 0:
        snake_head.setheading(180)
def d():
    if snake_head.heading() != 180:
        snake_head.setheading(0)

def game():
    screen.onkeypress(key='w', fun=w)
    screen.onkeypress(key='s', fun=s)
    screen.onkeypress(key='a', fun=a)
    screen.onkeypress(key='d', fun=d)

game()
score.write(f'Score: 0', align='center', font=('Arial', 20, 'bold'))
while game_is_on:
    sleep(speed)
    heading = int(snake_head.heading())
    snake_length()
    if heading == 0:
        x = snake_head.xcor() + 40
        y = snake_head.ycor()
    elif heading == 90:
        x = snake_head.xcor()
        y = snake_head.ycor() + 40
    elif heading == 180:
        x = snake_head.xcor() - 40
        y = snake_head.ycor()
    elif heading == 270:
        x = snake_head.xcor()
        y = snake_head.ycor() - 40
    snake_head.goto(x, y)
    collision()

screen.exitonclick()
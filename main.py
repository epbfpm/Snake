from snake import Snake
from time import sleep
from screen_elements import Border, Text
from turtle import Screen
from food import Food

# global parameters
skl = 4
scr = 0
spd = 0.3
# screen config
screen = Screen()
screen.colormode(255)
screen.screensize(canvwidth=80 *skl, canvheight=50 *skl, bg='#a4be3d')
screen.listen()
screen.tracer(0)
# border
border = Border()
border.setposition(-screen.canvwidth/2, screen.canvheight/2)
border.pendown()
border.setposition(-screen.canvwidth/2, -screen.canvheight/2)
border.setposition(screen.canvwidth/2, -screen.canvheight/2)
border.setposition(screen.canvwidth/2, screen.canvheight/2)
border.setposition(-screen.canvwidth/2, screen.canvheight/2)
# text on screen
text = Text(skl)
text.scoreboard(scr)
# snake parameters
segment_size = skl
snake = Snake(segment_size)
# food parameters
food_size = skl
food = Food(food_size)
# moving
screen.onkeypress(key='w', fun=snake.w)
screen.onkeypress(key='s', fun=snake.s)
screen.onkeypress(key='a', fun=snake.a)
screen.onkeypress(key='d', fun=snake.d)
screen.listen()

# game
game_is_on = True
while game_is_on:
    screen.update()
    sleep(spd)
    snake.move()
    #collision with wall
    if snake.head.xcor() > screen.canvwidth/2 - 1 or snake.head.ycor() > screen.canvheight/2 - 1 or snake.head.xcor() < -screen.canvwidth/2 + 1 or snake.head.ycor() < -screen.canvheight/2 + 1:
        text.gameover()
        game_is_on = False
    # collision with itself
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            print(snake.head.pos())
            print(snake.segment_positions)
            text.gameover()
            game_is_on = False
    # collision with food
    if snake.head.distance(food) < 10:
        print(f'food{food.pos()}')
        print(f'snake {snake.head.pos()}')
        scr += 1
        snake.add_segment(food.pos())
        text.scoreboard(scr)
        food.refresh()
    # speed
    if scr % 3 == 0 and scr < 18:
        spd = 0.3 - scr * 0.05







screen.exitonclick()
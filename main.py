from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('light green')
screen.title('snakk')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.update()

# Turns.
screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'Right')

# Move the snake.
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.body[0].distance(food) < 15:
        snake.extend()
        food.refresh()
        score.refresh()

    # Detect collision with a wall.
    if snake.body[0].xcor() > 295 or snake.body[0].xcor() < -300 \
            or snake.body[0].ycor() > 300 or snake.body[0].ycor() < -290:
        score.game_over()
        game_on = False

    # Detect collision with the tail.
    for segment in snake.body[1:]:
        if snake.body[0].distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()

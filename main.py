from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


screen = Screen()
screen.tracer(0)
#create a snake and turn off the tracer


snake = Snake()
#create a snake


screen.listen()
#add commands for the snake

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


food = Food()
scored = Score()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
#create food for the snake and screen for the game


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    #create an animation
    snake.move()
    #pursue the snake to move non-stop


    if snake.head.distance(food) <= 15:
    #the snake eats food: create new food and change the score
        food.refresh()
        snake.neo()
        scored.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #the snake touched the border: create a new snake and reset the score to 0
        scored.reset()
        snake.reset()


    for segment in snake.snakes[1:]:
    #the snake touched the own body(except the head): create a new snake and reset the score to 0
        if snake.head.distance(segment) < 10:
            scored.reset()
            snake.reset()


screen.exitonclick()
#finish the game by clicking the screen out of the game screen
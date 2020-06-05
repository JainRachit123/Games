from turtle import *
from random import *
from time import *

# variables to store scores
high_score = 0
score = 0
d = 0.1

# setting up screen
screen = Screen()
screen.title('This is made by Rachit Jain')
screen.setup(420, 420, 470, 0)
screen.bgcolor('green')
screen.tracer(0)

# setting pen for score
pen = Turtle()
pen.penup()
pen.hideturtle()
pen.goto(0, 170)
pen.color('white')
pen.write('Score: {}  High Score: {}'.format(score, high_score), align='center',
          font=("Courier", 18, "normal"))

# snakes food
food = Turtle()
food.speed(0)
food.shape('circle')
food.shapesize(0.3)
food.color('red')
food.penup()
food.goto(50, 0)

# snake head
head = Turtle()
head.speed(0)
head.shape('square')
head.shapesize(0.5)
head.color('black')
head.penup()
head.direction = 'stop'

snake = []


# function to define movement of snake
def move():
    if head.direction == 'Up':
        y = head.ycor()
        head.sety(y + 5)
    elif head.direction == 'Down':
        y = head.ycor()
        head.sety(y - 5)
    elif head.direction == 'Right':
        x = head.xcor()
        head.setx(x + 5)
    elif head.direction == 'Left':
        x = head.xcor()
        head.setx(x - 5)
    else:
        head.speed(0)
        head.goto(0, 0)


# function to change direction of movement
def change(x, y):
    if x == 0:
        if y == 5:
            head.direction = 'Up'
        else:
            head.direction = 'Down'
    else:
        if x == 5:
            head.direction = 'Right'
        else:
            head.direction = 'Left'


# functions to get inputs from keyboard
listen()
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')

try:
    print("Game Started")
    while True:
        update()

        # checking if the snake hit the boundary
        if -210 > head.xcor() or head.xcor() > 210 or -210 > head.ycor() or head.ycor() > 210:
            sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            for body in snake:
                body.goto(1000, 1000)

            score = 0   # resetting score
            snake.clear()   # making the snake list empty
            pen.clear()
            pen.write('Score: {}  High Score: {}'.format(score, high_score), align='center',
                      font=("Courier", 18, "normal"))
            print('Start Again')

        # when the snake eats the food
        if head.distance(food) < 10:
            food.goto(randrange(-200, 200), randrange(-200, 200))

            # initializing a new segment for body
            segment = Turtle()
            segment.speed(0)
            segment.shape('square')
            segment.shapesize(0.5)
            segment.color('grey')
            segment.penup()
            snake.append(segment)

            # updating score and delay
            score += 10
            d -= 0.001

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write('Score: {}  High Score: {}'.format(score, high_score), align='center',
                      font=("Courier", 18, "normal"))

        # moving the body
        for index in range(len(snake) - 1, 0, -1):
            snake[index].goto(snake[index-1].position())

        # moving the segment at 0 index
        if len(snake) > 0:
            snake[0].goto(head.position())

        move()

        # checking if the head collide with body
        for segments in snake   :
            if segments.distance(head) < 5:
                sleep(1)
                head.goto(0, 0)
                head.direction = 'stop'

                for body in snake:
                    body.goto(1000, 1000)

                score = 0
                snake.clear()
                pen.clear()
                pen.write('Score: {}  High Score: {}'.format(score, high_score), align='center',
                          font=("Courier", 18, "normal"))
                print("Start Again")

        sleep(d)

except :
    print('Game Closed')

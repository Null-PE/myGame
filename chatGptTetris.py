import turtle
import random

# Initialize the game window
turtle.setup(600, 600)
turtle.title("Tetris")
turtle.bgcolor("black")

# Create the game board
board = turtle.Turtle()
board.speed(0)
board.color("white")
board.penup()
board.setposition(-250, -250)
board.pendown()
for i in range(4):
    board.forward(500)
    board.right(90)
board.hideturtle()

# Define the shapes of the Tetrominoes
tetrominoes = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    [[0, 0], [1, 0], [2, 0], [0, 1]],
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 0], [1, 0], [1, 1], [1, 2]]
]

# Create a Turtle to represent each Tetromino
tetromino = turtle.Turtle()
tetromino.speed(0)
tetromino.color("white")
tetromino.penup()
tetromino.setposition(0, 250)
tetromino.pendown()

# Move the Tetromino down by one row every 50 milliseconds
def move_down():
    y = tetromino.ycor()
    y -= 25
    tetromino.sety(y)

# Main game loop
while True:
    shape = tetrominoes[random.randint(0, 6)]
    for block in shape:
        tetromino.stamp()
        tetromino.forward(25)
        tetromino.right(90)
        tetromino.forward(25)
        tetromino.left(90)
    turtle.ontimer(move_down, 50)

turtle.done()

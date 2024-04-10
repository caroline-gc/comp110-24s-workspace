"""Turtle Project: Tried something fun in function lake by using ".circle" and also used random function to make fish randomly appear at places in my lake. In the going_fishing function I broke up a complex function into a simpler repeating function by calling the fish function a certain number of times."""

__author__ = "730394278"

import random
from turtle import Turtle, colormode, done, tracer, update
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    turtle: Turtle = Turtle()
    ground(turtle, -700, -500)
    sky(turtle, -700, 0)
    mountain(turtle, -700, 0)
    lake(turtle, 0, -400)
    fish(turtle, 0, -200)
    going_fishing(turtle, 3)
    update()
    done()


def ground(turtle: Turtle, x: float, y: float) -> None:
    """Draw the rectangle for the green ground starting at the bottom lefthand corner."""
    turtle.speed(50)
    turtle.color("green", "green")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    long_side: int = 1500
    short_side: int = 500
    i: int = 0
    while (i < 2):
        turtle.forward(long_side)
        turtle.left(90)
        turtle.forward(short_side)
        turtle.left(90)
        i = i + 1
    turtle.end_fill()
    
 
def sky(turtle: Turtle, x: float, y: float) -> None:
    """Draw the rectangle for the blue sky starting at the top left hand corner of the ground block."""
    turtle.speed(50)
    turtle.pencolor(100, 150, 255)
    turtle.fillcolor(100, 150, 255)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    long_side: int = 1500
    short_side: int = 500
    i: int = 0
    while (i < 2): 
        turtle.forward(long_side)
        turtle.left(90)
        turtle.forward(short_side)
        turtle.left(90)
        i = i + 1
    turtle.end_fill()
    

def mountain(turtle: Turtle, x: float, y: float) -> None:
    """Draw the triangle for the five grey mountains with each mountain starting at the point the last one ended."""
    j: int = 0
    while (j < 5):
        turtle.speed(50)
        turtle.pencolor(50, 50, 50)
        turtle.fillcolor(50, 50, 50)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        i: int = 0
        while (i < 3):
            turtle.forward(300)
            turtle.left(120)
            i = i + 1
        turtle.end_fill()
        x += 300
        j = j + 1


def lake(turtle: Turtle, x: float, y: float) -> None:
    """Try something fun: Used the circle function from the Turtle Documentation page to draw the circle for the blue lake in the center of the ground."""
    turtle.speed(50)
    turtle.color("blue", "blue")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(175)
    turtle.end_fill()


def fish(turtle: Turtle, x: int, y: int) -> None:
    """Draw the rhombus for the first orange fish and its eye to appear at a random point."""
    turtle.speed(50)
    turtle.color("orange", "orange")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    long_side: int = 50
    i: int = 0
    while (i < 2): 
        turtle.forward(long_side)
        turtle.left(140)
        turtle.forward(long_side)
        turtle.left(40)
        i = i + 1
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x + 25, y + 10)
    turtle.pendown()
    turtle.dot(10, "black")


def going_fishing(turtle: Turtle, fish_friends: int) -> None:
    """Breaks up complex functions and Uses Recursion: Having a certain number of other fish show up in random positions in the lake using the fish function."""
    i: int = 0
    if i == fish_friends:
        return None
    else:
        while (i < fish_friends):
            fish(turtle, random.randint(-100, 100), random.randint(-300, -50))
            i += 1
     

main()


__name__ == "__main__"

"""Turtle Tutorial."""

from turtle import Turtle, colormode, done
colormode(255)


# turtle_object_variable.method_name()

leo: Turtle = Turtle() #constructs a new Turtle object

leo.speed(25)
#leo.hideturtle()

leo.pencolor(32, 67, 93)
leo.fillcolor(0, 0, 0) #all 0 black, all 255 white 

leo.penup()
leo.goto(-200, -100)
leo.pendown()

# leo.pencolor("pink") pen only
# leo.fillcolor(32, 67, 93) fill
# leo.color("green", "yellow") both

leo.begin_fill()
i: int = 0
while (i < 3): # triangle
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

done()




bob: Turtle = Turtle()

bob.speed(50)

bob.pencolor(32, 67, 93)
bob.fillcolor(0, 0, 0) #all 0 black, all 255 white 

bob.penup()
bob.goto(-200, -100)
bob.pendown()

# leo.pencolor("pink") pen only
# leo.fillcolor(32, 67, 93) fill
# leo.color("green", "yellow") both

bob.begin_fill()
side_length: int = 300
i: int = 0
while (i < 3): # triangle
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
    side_length = side_length * 0.97
bob.end_fill()

done()









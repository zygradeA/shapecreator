import turtle as pen
import math as m
turt = pen



def shapecreate(numberofside,sidelength,angle):
    for i in range(numberofside):
        pen.forward(sidelength)
        pen.right(angle)


def triangle(base,height,x,y,edge_thickness = None,edge_colour = None,fill_colour = None):
    pen.penup()
    turt.goto(x,y)
    turt.setheading(0)
    turt.pen(pensize=edge_thickness, pencolor=edge_colour, fillcolor=fill_colour)
    turt.pendown()
    turt.begin_fill()

    angle = m.degrees(m.atan(2*height/base))
    side = m.sqrt(height**2+((base**2)/4))
    #thank you so much to the relief math and science teacher i had in science for teaching me how to do these equations

    turt.forward(base)
    turt.setheading(180)
    turt.right(angle)
    turt.forward(side)
    turt.penup()
    turt.goto(x,y)
    turt.pendown()
    turt.setheading(0)
    turt.left(angle)
    turt.forward(side)

    turt.end_fill()


def rectangle(sidelength,sidelengthmultiplier):
    for i in range(2):
        pen.right(90)
        pen.forward(sidelength*sidelengthmultiplier)
        pen.right(90)
        pen.forward(sidelength)

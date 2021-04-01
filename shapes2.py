import turtle as pen

def shapecreate(numberofside,sidelength,angle):
    for i in range(numberofside):
        pen.forward(sidelength)
        pen.left(angle)
    def triangle(base,height):
        angle = m.degrees(m.atan(2*height/base))
        side = m.sqrt(height**2+((base**2)/4))
    #thank you so much to the relief math and science teacher i had in science for teaching me how to do these equations

        pen.forward(base)
        pen.setheading(180)
        pen.right(angle)
        pen.forward(side)
        pen.penup()
        pen.pendown()
        pen.setheading(0)
        pen.left(angle)
        pen.forward(side)
    return shapecreate




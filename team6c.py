import turtle as t

# bg colour
BG_COLOUR = "WHITE"
t.bgcolor("WHITE")


# screen 
screen = t.Screen()
screen.setworldcoordinates(0,0,1000,1000)


#speed cus im not waiting
t.speed(0)

def head():
    t.penup()
    t.goto(500,150)
    t.pendown()
    t.circle(220)
    
    # smile
    t.penup()
    t.goto(450,220)
    t.pendown()
    #orientation of the arrow u cant see it at full speed lower for demonostration
    t.setheading(270)
    t.circle(50,180)
    t.setheading(0)


    #left eye
    t.penup()
    t.goto(400,400)
    t.pendown()
    t.circle(15)

    #right eye
    t.penup()
    t.goto(600,400)
    t.pendown()
    t.circle(15)

    #nose


head()


def chief_hat():
    # middle
    t.penup()
    t.goto(500,500)
    t.pendown()

    #middle circle
    t.fillcolor("BLACK")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    

    #left circle
    t.penup()
    t.backward(150)
    t.pendown()
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    #right circle
    t.penup()
    t.forward(300)
    t.pendown()
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.penup()

    t.goto(500,500)
    t.pendown()
    t.pencolor("WHITE")
    t.fillcolor("WHITE")
    t.begin_fill()
    t.circle(90)
    t.end_fill()
    

    #left circle
    t.penup()
    t.backward(150)
    t.pendown()
    t.begin_fill()
    t.circle(90)
    t.end_fill()

    #right circle
    t.penup()
    t.forward(300)
    t.pendown()
    t.begin_fill()
    t.circle(90)
    t.end_fill()

    #base
    t.penup()
    t.goto(300,550)
    t.pendown()
    t.pencolor("BLACK")
    t.fillcolor("BLACK")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()
    

    t.penup()
    t.goto(325,535)
    t.pendown()
    t.fillcolor("WHITE")
    t.begin_fill()
    for i in range(2):
        t.forward(350)
        t.right(90)
        t.forward(75)
        t.right(90)
    t.end_fill()

chief_hat()

t.done()


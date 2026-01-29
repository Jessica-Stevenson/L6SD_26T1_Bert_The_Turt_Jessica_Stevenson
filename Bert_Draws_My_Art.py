import turtle
s = turtle.getscreen()
Bert = turtle.Turtle()

Bert.pen(pencolor="#8b1017", fillcolor="#d85d4a", pensize=10)


Bert.begin_fill()
Bert.penup()
Bert.goto(-150,90)
Bert.right(50)
Bert.pendown()
#first Curve
Bert.circle(100,-140)

#little hair piece
Bert.left(90)
Bert.forward(10)
Bert.left(180)
Bert.forward(10)
Bert.right(15)
Bert.forward(10)
Bert.circle(-20,30)
Bert.forward(20)
Bert.right(140)
Bert.forward(40)

#Fringe 1
Bert.right(180)
Bert.forward(10)
Bert.right(90)
Bert.circle(-100,120)
Bert.right(160)
Bert.circle(100, 80)



turtle.done()
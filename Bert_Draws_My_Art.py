import turtle
s = turtle.getscreen()
Bert = turtle.Turtle()

Bert.pen(pencolor="#8b1017", fillcolor="#d85d4a", pensize=10, speed=80)


Bert.begin_fill()
Bert.penup()
Bert.goto(-150,90)
Bert.right(50)
Bert.pendown()
#Curve
Bert.circle(100,-140)

#Little hair piece
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

#Fringe
Bert.right(180)
Bert.forward(10)
Bert.right(90)
Bert.circle(-100,120)
Bert.right(160)
Bert.circle(100, 80)
Bert.left(40)
Bert.circle(90, 120)
Bert.goto(-150,90)
Bert.end_fill()

#Moving bert to next part
Bert.penup()
Bert.left(50)
Bert.forward(58)
Bert.pendown()

Bert.pen(pencolor="#f19a95", fillcolor="#d85d4a", pensize=10, speed=80)


#Face
Bert.right(20)
Bert.forward(60)
Bert.left(60)
Bert.forward(50)

turtle.done()
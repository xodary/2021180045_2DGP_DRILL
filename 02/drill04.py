import turtle

i = 0
while i < 6:
    turtle.penup()
    turtle.goto(0,100 * i)
    turtle.pendown()
    turtle.forward(500)
    i += 1

turtle.left(90)
i = 0
while i < 6:
    turtle.penup()
    turtle.goto(100*i,0)
    turtle.pendown()
    turtle.forward(500)
    i += 1
    
turtle.exitonclick()

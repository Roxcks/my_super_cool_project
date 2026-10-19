import turtle

turtle.speed(10)

def draw_triangle(size):
    angle = 120
    turtle.pendown()
    for _ in range(3):
        turtle.forward(size)
        turtle.right(angle)
    turtle.penup()
    turtle.forward(size)
    turtle.left(60)


side = 80
for _ in range(6):
    draw_triangle(side)
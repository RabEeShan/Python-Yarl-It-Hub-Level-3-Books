import turtle

from itertools import cycle
colors = cycle(['blue', 'orange', 'purple', 'red', 'green', 'yellow'])


def draw_circle(size,angle,shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+4, angle+31,shift+1)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(20)
draw_circle(30,0,1)


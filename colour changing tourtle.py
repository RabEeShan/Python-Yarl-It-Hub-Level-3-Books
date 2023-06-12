import turtle

from itertools import cycle
colors = cycle(['Goldenrod', 'Purple', 'Lawn Green', 'Seashell', 'Light blue', 'yellow'])


def draw_circle(size,angle,shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+5, angle+1,shift+1)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(50)
draw_circle(40,2,3)

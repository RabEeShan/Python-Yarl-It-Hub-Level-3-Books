import turtle

from itertools import cycle
colors = cycle(['Red', 'Purple', 'Green', 'Orange', 'Light blue', 'yellow'])


def draw_circle(size):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    draw_circle(size+5)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(5)
draw_circle(30)

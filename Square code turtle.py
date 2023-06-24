import turtle

from itertools import cycle
colors = cycle(['red', 'Purple', 'Orange', 'green', 'blue', 'yellow'])


def draw_shape(size,angle,shift):
    turtle.pencolor(next(colors))
    next_shape=''
    if shape=='circle':
     turtle.circle(size)
     next_shape='square'
    elif shape=='square':
      'for 1 in range(4)'
    turtle.forward('size.2')
    turtle.left(90)

'next_shape'='circle'

    turtle.right(angle)
    turtle.forward(shift)
    draw_shape(size+5,angle+1,shift+1,next_shape)
turtle.bgcolor('red')
turtle.speed('fast')
turtle.pensize(4)
draw_shape(30,0,1,'circle')

    
         

    
    
    
    

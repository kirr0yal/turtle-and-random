import turtle as t
import random

t.setup(900, 900)
t.setpos(-50, 50)
t.bgcolor('black')
t.pensize(3)
t.speed(8)

colors = ['white', 'red', 'green', 'blue', 'cyan', 'magenta',
          'yellow', 'orange', 'purple', 'brown', 'pink']


def hexagon(side):
    t.shape('turtle')
    for _ in range(6):
        random_color = random.choice(colors)
        t.pencolor(random_color)
        t.forward(side)
        t.left(60)
    t.forward(side)
    t.right(60)


for _ in range(6):
    hexagon(80)

t.done()

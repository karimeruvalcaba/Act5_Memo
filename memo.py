from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
taps = 0  
tile_colors = ['#' + ''.join(choice('0123456789ABCDEF') for _ in range(6)) for _ in range(32)] * 2  # Generate a list of random colors for tiles

def square(x, y, fill_color):
    "Draw colored square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    begin_fill()
    color('black', fill_color)
    for _ in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global taps  
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        taps += 1  

def draw():
    "Draw image and tiles."
    global taps  
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            fill_color = tile_colors[tiles[count]]  # Assigning color based on tile index
            square(x, y, fill_color)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()

    if all(not tile_hidden for tile_hidden in hide):
        print("Congratulations! You've uncovered all the tiles in", taps, "taps.")
        return

    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

import turtle as t
import math

screen = t.Screen()
t.hideturtle()
t.speed(0)
screen.tracer(0,0)

WIDTH, HEIGHT = screen.window_width(), screen.window_height()
DIAGONAL = math.hypot(WIDTH, HEIGHT)


def night_sky():
    start_color = (0.52156, 0.35294, 0.53333) # light purple
    end_color = (0.02745, 0.039215, 0.2) # deep purple-blue

    deltas = [(hue - start_color[index]) / HEIGHT for index, hue in enumerate(end_color)]

    t.color(start_color)

    t.up()
    t.goto(-WIDTH/2, HEIGHT/2)
    t.down()

    direction = 1

    for distance, y in enumerate(range(HEIGHT//2, -HEIGHT//2, -1)):
        # compute intermediate color
        t.forward(WIDTH * direction)
        t.color([start_color[i] + delta * distance for i, delta in enumerate(deltas)])
        t.sety(y)

        direction *= -1

    screen.tracer(True)


def tall_oval(r):
    t.left(45)
    for half in range(2):
        t.circle(r,90)
        t.circle(r/4,90)
    t.setheading(0)


def flat_oval(r):
    t.right(45)
    for half in range(2):
        t.circle(r,90)
        t.circle(r/25,90)
    t.setheading(0)


def stripe(l, ps, color):
    t.pensize(ps)
    t.down()
    t.pencolor(color)
    t.forward(l)


def moon():
    t.speed(0)
    t.up()
    t.goto(0,150)
    t.down()
    t.pensize(6)
    t.pencolor("#aa99c9")
    t.begin_fill()
    t.fillcolor('#EDE3FF')
    t.circle(350)
    t.end_fill()

    t.up()
    t.goto(40,185)
    t.down()
    t.circle(60)
    t.up()
    t.goto(-150, 260)
    t.down()
    t.circle(50)
    t.up()
    t.goto(180, 260)
    t.down()
    t.circle(40)
    t.up()
    t.goto(-90, 200)
    t.down()
    t.circle(20)


def kirby_body():
    t.up()
    t.goto(-150, -150)
    t.down()
    t.pencolor('#E90071')
    t.pensize(3)
    t.begin_fill()
    t.fillcolor('#FFBBDB')
    t.circle(100)
    t.end_fill()


def eyes():
    t.up()
    t.pencolor('#290323')
    t.pensize(1)
    t.goto(-200, -60)
    t.down()
    t.fillcolor('#290323')
    t.begin_fill()
    tall_oval(20)
    t.end_fill()
    t.up()
    t.goto(-201, -60)
    t.down()
    t.fillcolor('#491bd1')
    t.begin_fill()
    tall_oval(15)
    t.end_fill()
    t.up()
    t.goto(-202, -53)
    t.down()
    t.fillcolor('#290323')
    t.begin_fill()
    tall_oval(10)
    t.end_fill()
    t.up()
    t.goto(-202, -43)
    t.down()
    t.fillcolor('#f7f5ff')
    t.begin_fill()
    tall_oval(8)
    t.end_fill()

# other eye
    t.up()
    t.goto(-150, -60)
    t.down()
    t.fillcolor('#290323')
    t.begin_fill()
    tall_oval(20)
    t.end_fill()
    t.up()
    t.goto(-151, -60)
    t.down()
    t.fillcolor('#491bd1')
    t.begin_fill()
    tall_oval(15)
    t.end_fill()
    t.up()
    t.goto(-152, -53)
    t.down()
    t.fillcolor('#290323')
    t.begin_fill()
    tall_oval(10)
    t.end_fill()
    t.up()
    t.goto(-152, -43)
    t.down()
    t.fillcolor('#f7f5ff')
    t.begin_fill()
    tall_oval(8)
    t.end_fill()


def witch_hat():
    t.up()
    t.pencolor('#421b4f')
    t.pensize(2)
    t.goto(-230, 40)
    t.down()
    t.right(10)
    t.fillcolor('#7b3991')
    t.begin_fill()
    flat_oval(150)
    t.end_fill()

    t.up()
    t.goto(-180, 40)
    t.setheading(40)
    t.down()
    t.fillcolor('#7b3991')
    t.begin_fill()
    t.forward(100)
    t.setheading(2)
    t.forward(135)
    t.left(28)
    t.back(98)
    t.left(25)
    t.back(61)
    t.left(108)
    t.pencolor('#7b3991')
    t.forward(97)
    t.end_fill()

    t.up()
    t.goto(-88,10)
    t.forward(94)
    t.pencolor('#E90071')
    t.left(130)
    t.pensize(8)
    t.down()
    t.circle(62,98)


def broom():
    t.up()
    t.goto(-250,-140)
    t.pensize(2)
    t.pencolor('#36230d')
    t.setheading(-5)
    t.down()
    t.back(40)
    t.forward(270)

    t.setheading(265)
    t.begin_fill()
    t.fillcolor('#543a1c')
    t.forward(15)
    t.right(90)
    t.forward(270)
    t.right(90)
    t.forward(15)
    t.end_fill()

    t.up()
    t.goto(-22, -175)
    t.fillcolor('#d4ad84')
    t.begin_fill()
    t.setheading(-5)
    t.down()
    t.left(-90)
    t.pencolor('#80684f')
    t.circle(30, 90)

    t.forward(75)
    t.left(90)
    t.forward(20)
    t.end_fill()

    t.up()
    t.goto(-21, -160)
    t.end_fill()
    t.down()
    t.begin_fill()
    t.fillcolor('#d4ad84')
    t.setheading(85)
    t.circle(-20, 90)
    t.forward(85)
    t.right(89)
    t.forward(46)
    t.up()
    t.goto(-21, -175)
    t.end_fill()

    #broom stripes
    t.goto(82, -199)
    t.setheading(175)
    stripe(15, 2, '#80684f')
    t.up()
    t.goto(83, -184)
    stripe(15, 2, '#80684f')
    t.up()
    t.goto(84, -168)
    stripe(15, 2, '#80684f')

    t.up()
    t.goto(-24, -175)
    t.setheading(85)
    stripe(15,7,'#E90071')


def broom_foot():
    t.pensize(3)
    t.pencolor('#E90071')
    t.up()
    t.goto(-165, -195)
    t.setheading(-10)
    t.begin_fill()
    t.fillcolor('#D12754')
    t.down()
    tall_oval(31)
    t.end_fill()


def other_foot():
    t.pensize(3)
    t.pencolor('#E90071')
    t.up()
    t.goto(-120,-199)
    t.setheading(-10)
    t.begin_fill()
    t.fillcolor('#D12754')
    t.down()
    tall_oval(37)
    t.end_fill()


def arms():
    t.pensize(2)
    t.up()
    t.goto(-180, -120)
    t.down()
    t.setheading(0)
    t.right(180)
    t.begin_fill()
    t.fillcolor('#FFBBDB')
    t.circle(19, 280)
    t.end_fill()

    t.up()
    t.goto(-205, -120)
    t.down()
    t.setheading(0)
    t.right(50)
    t.begin_fill()
    t.fillcolor('#FFBBDB')
    t.circle(-17, 295)
    t.end_fill()


def smile():
    t.up()
    t.goto(-190, -80)
    t.pensize(1)
    t.setheading(0)
    t.left(-90)
    t.down()
    t.circle(10, 180)


def blush():
    t.up()
    t.goto(-232, -69)
    t.setheading(0)
    t.begin_fill()
    t.fillcolor('#D12754')
    t.down()
    flat_oval(9)
    t.end_fill()

    t.up()
    t.goto(-140, -69)
    t.setheading(0)
    t.begin_fill()
    t.fillcolor('#D12754')
    t.down()
    flat_oval(9)
    t.end_fill()


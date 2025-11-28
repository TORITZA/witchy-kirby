from drawers import *

screen = t.Screen()
t.hideturtle()
t.speed(0)
screen.tracer(0,0)

WIDTH, HEIGHT = screen.window_width(), screen.window_height()
DIAGONAL = math.hypot(WIDTH, HEIGHT)


if __name__ == '__main__':
    screen.addshape('starTwoTwo.gif')
    screen.addshape('ghostOne.gif')
    screen.addshape('ghostTwo.gif')

    night_sky()
    moon()

    kirby_body()
    eyes()
    witch_hat()
    broom_foot()
    broom()
    other_foot()
    arms()
    smile()
    blush()

    t.up()
    t.goto(250, -230)
    t.shape('starTwoTwo.gif')
    t.showturtle()
    t.stamp()
    t.down()

    t.up()
    t.goto(-280, 140)
    t.shape('starTwoTwo.gif')
    t.stamp()
    t.down()

    t.up()
    t.goto(300, 150)
    t.shape('starTwoTwo.gif')
    t.stamp()
    t.down()

    t.up()
    t.goto(-375, -70)
    t.shape('starTwoTwo.gif')
    t.stamp()
    t.down()

    t.up()
    t.goto(170, 40)
    t.shape('ghostTwo.gif')
    t.stamp()
    t.down()

    t.up()
    t.goto(-320, -270)
    t.shape('ghostOne.gif')
    t.stamp()
    t.down()


    screen.update()

    screen.exitonclick()


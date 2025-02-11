def turn_right():
    for i in range(0, 3):
        turn_left()


def do_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for i in range(0, 6):
    do_hurdle()
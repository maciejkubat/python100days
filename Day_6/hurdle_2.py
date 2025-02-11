def turn_right():
    for i in range(0, 3):
        turn_left()


def do_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        do_hurdle()
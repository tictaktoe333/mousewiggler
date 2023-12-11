#!/usr/bin/python3
# Mouse wiggler

import mouse
from random import randrange

from time import sleep


def setup():
    """Returns a tuple containing the mouse's starting XY position."""
    return mouse.get_position()


def run(start_position):
    """Find current position of mouse and run main loop."""
    current = start_position
    print(f"{current}")

    while True:
        x_change = randrange(11, 50, 1)
        y_change = randrange(11, 50, 1)
        print(current[0])
        mouse.move(current[0] + x_change, current[1] + y_change, True, duration=1)
        waiting = randrange(50, 61, 1)
        print(waiting)
        sleep(waiting)


if __name__ == "__main__":
    start_position = setup()
    run(start_position)

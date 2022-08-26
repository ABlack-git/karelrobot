from stanfordkarel import *
from enum import Enum


class Orientation(Enum):
    NORTH = 1
    EAST = 2
    WEST = 3
    SOUTH = 4


x_coord = 0
y_coord = 0
current_orientation = Orientation.NORTH


def step():
    """ Implement and use this function instead of move. This function should help you update coordinates while you
    move"""
    pass


def update_coordinates(direction: Orientation):
    """Update x and y coordinates depending on the direction in which you move"""
    pass


def rotate_left():
    """ Implement and use this function instead of turn_left. This function should help you keep track of orientation
    when you turn Karel"""
    pass


def clean_wall():
    """Clean one wall to the nearest corner"""
    pass


def clean_beeper():
    """
    Use corner_color_is(color) function to check the color of a corner. Possible values for color are RED, GREEN, BLUE,
    YELLOW, BLACK.

    When you determined the color of the corner move beeper according to this rules:

    If corner is RED pick beeper, face north and move until there are no walls on left and right, put beeper.
    If corner is GREEN pick beeper, face east and move until there are no walls on left and right, put beeper.
    If corner is BLUE pick beeper, face west and move until there are no walls on left and right, put beeper.
    If corner is YELLOW pick beeper, face south and move until there are no walls on left and right, put beeper.
    If corner is BLACK just pick beeper.
    If corner doesn't have any of the mentioned above colors just move beeper away from wall as in the previous
    assignment
    """
    pass


def main():
    """ Write your main program """


if __name__ == '__main__':
    run_karel_program("20x15_adv_wall_cleaning")

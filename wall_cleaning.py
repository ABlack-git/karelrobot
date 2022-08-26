from stanfordkarel import *

"""In this task you should make Karel to move all the beepers away from walls (e.g. move it one position away from 
wall). The room has a rectangular shape and doesn't have any obstacles. There are no beepers in the corner. Initial 
position of Karel will be always near a wall but not always in corner. Start by going to the nearest corner in the 
direction where Karl is facing, when you get to the nearest corner position Karl such that he has a wall on the right
and behind him. Clean the walls. In the end Karel should be in the corner of the last wall you ckeanedd."""


def go_to_corner():
    """ Make Karel got to corner. After Karel has moved to corner he should have a wall on the right and
    behind him"""


def clean_one_wall():
    """ Make Karel go along one wall. If he encounters a beeper he should move it from the wall"""


def main():
    """ Write your main program """


if __name__ == '__main__':
    run_karel_program("5_by_5_move_beepers")

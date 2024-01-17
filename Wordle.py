# File: Wordle.py
# GROUP 13
"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        # initialize some variables
        current_col = 0
        userword = ""
        
        # get the user input
        while current_col < N_COLS:
            userword += gw.get_square_letter(gw.get_current_row(), current_col)
            current_col += 1

        userword = userword.lower()
        print(userword)

        # check if real word
        if userword in FIVE_LETTER_WORDS:
            gw.show_message("Completed Milestone 2!")
        else:
            pass
        # insert msg if not real word

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    newword = random.choice(FIVE_LETTER_WORDS)

    col = 0
    while col < N_COLS:
        gw.set_square_letter(gw.get_current_row(), col, newword[col])
        col += 1

# Startup code

if __name__ == "__main__":
    wordle()

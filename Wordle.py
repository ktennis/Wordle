# File: Wordle.py
# GROUP 13
"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
                
    def enter_action(s):

        # initialize some variables
        current_col = 0
        userword = ""   
        current_row = gw.get_current_row()
        
     
        # get the user input
        while current_col < N_COLS:
            userword += gw.get_square_letter(gw.get_current_row(), current_col)
            current_col += 1

        print(newword)
        

        for char in userword:
            if char in newword:
                gw.set_key_color(char, CORRECT_COLOR)
            # elif char in newword:
            #     gw.set_key_color(char, PRESENT_COLOR)
            else:
                gw.set_key_color(char, MISSING_COLOR)
                
        
        # Update color for the top row
        for col in range(N_COLS):
            top_row_letter = gw.get_square_letter(current_row, col)
            if top_row_letter == newword[col]:
                gw.set_square_color(current_row, col, CORRECT_COLOR)
            elif top_row_letter in newword:
                gw.set_square_color(current_row, col, PRESENT_COLOR)
            else:
                gw.set_square_color(current_row, col, MISSING_COLOR)
                

        print(userword)
        userword = userword.lower()

        # check if real word
        if userword in FIVE_LETTER_WORDS:
            gw.show_message("Completed Milestone 2!")
        else:
            gw.show_message("Not in word list")
            
        #end game once word is guessed
        if userword == newword.lower():
            gw.show_message("Congratulations! You guessed the word correctly!")
            return
            
        # Move to the next row
        current_row += 1
        if current_row < N_ROWS:
            gw.set_current_row(current_row)
            
        # insert msg if not real word

    newword = random.choice(FIVE_LETTER_WORDS).upper()

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    col = 0
    while col < N_COLS:
        gw.set_square_letter(gw.get_current_row(), col, newword[col])
        col += 1
        

# Startup code

if __name__ == "__main__":
    wordle()

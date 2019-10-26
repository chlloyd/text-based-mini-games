import random

from lives import LIVES

with open('words.txt') as f:
    lines = f.read().splitlines()

def random_word():
    return lines[random.randint(0, len(lines))].lower()

def first_message(word):
    return "Welcome to hangman. Your word is " + str(
        len(word)) + " letters long. \nYou currently have 10 lives left. \nEnter your first letter! \n" + LIVES[0]

def run_game(input, word):
    hearts = 10
    while hearts > 0:
        if len(input) != 1:
            print("Please enter 1 letter")
        else:
            if input in word:
                # create ---letter--- line
                pass
            else:
                hearts -= 1

run_game("aa", random_word())


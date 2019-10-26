import random

from lives import LIVES

with open('words.txt') as f:
    lines = f.read().splitlines()

action_list = []

first_time = True
word = ""
letters = []


def random_word():
    return lines[random.randint(0, len(lines))].lower()


def display_letters(letters):
    dashes = ""
    for w in word:
        if w in letters:
            dashes += w
        else:
            dashes += "-"
    return dashes


def first_message(word):
    return "Welcome to hangman. Your word is " + str(
        len(word)) + " letters long. \nYou currently have 10 lives left. \nEnter your first letter! \n" + LIVES[0]


def first_run():
    global first_time
    global word
    if first_time:
        word = random_word()
        message = first_message(word)
        first_time = False
        return message


def run_game(letter):
    first_run()
    hearts = 10
    if letter in word:
        letters.append(letter)
        return display_letters(letters)
    else:
        hearts -= 1


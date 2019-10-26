import random


class HangmanGame:
    def __init__(self):
        with open('words.txt') as f:
            self.lines = f.read().splitlines()

    def random_word(self):
        return self.lines[random.randint(0, len(self.lines))].lower()


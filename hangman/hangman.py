import random

from lives import LIVES


class HangmanGame:
    def __init__(self):
        with open('words.txt') as f:
            self.lines = f.read().splitlines()

    def random_word(self):
        return self.lines[random.randint(0, len(self.lines))].lower()

    def first_message(self, word):
        return "Welcome to hangman. Your word is " + str(len(word)) + " letters long"


    def run_game(self):
        word = self.random_word()
        print(self.first_message(word))
        """running = True
        while running == True:
            if letter in word:"""





playGame = HangmanGame()
playGame.run_game()


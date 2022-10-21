
"""
        responsibility:
            -to store a list of words and randomly pick one for game play, to turn chosen word into an array of the letters in the word

        attributes:
            -word list: an array storing the words that are possible options for game play
            -word: the word chosen for game play
            -letters: an array containing the letters in the word

        methods:
            -pick word: arguments: self. randomly chooses a word from the array based on index. store in word attribute
            -letters: arguments: self. Splits word into a array where each item is a single letter of the word in the correct order of the word. stores in letters attribute
"""
import random


class Word:
    def __init__(self):
        self._wordList = ["shark", "tiger", "pool", "beach", "water", "soccer", "tennis", "apple", "orange", "pizza"]
        self._word = self._wordList[random.randint(0, len(self._wordList) - 1)]
        self._letters = []

    def get_letters(self):
        self._letters = [i for i in self._word]
        return  self._letters

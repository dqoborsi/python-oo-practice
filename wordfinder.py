"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    def __init__(self, words_file):
        ...
        text = open(words_file)
        self.list_of_words = [word.strip() for word in text]


    def random(self):
        ...
        return random.choice(self.list_of_words)

test = WordFinder('words.txt')
print(test.random())
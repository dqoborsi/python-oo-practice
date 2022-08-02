from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    ...
    def __init__(self, words_file):
        text = open(words_file)
        self.list_of_words = [word.strip() for word in text if word.strip() and word[0] != '#']

test2 = SpecialWordFinder('words2.txt')
print("test2.random(): ", test2.random())
word = ''
print(bool(word.strip()))
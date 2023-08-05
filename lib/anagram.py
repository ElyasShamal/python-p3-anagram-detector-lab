# your code goes here!

class Anagram:
    
    def __init__(self, word):
        self.word = word

    def match(self, words_list):    
        anagrams = []
        sort_word = sorted(self.word.lower())

        for word in words_list:
            if sort_word == sorted(word.lower()) and self.word.lower() != word.lower():
                anagrams.append(word)

        return anagrams        
from words import words
import numpy as np

class Handler:
    def __init__(self, words) -> None:
        self.words = words
        self.word_list = np.array([])
        self.used_words = np.array([])
        self.prev_success = False

    def generate_word(self) -> str:
        random_word = np.random.choice(self.words, replace=False)
        self.used_words = np.append(self.used_words, random_word)
        return random_word
    
    def update_word_list(self):
        if len(self.word_list) == 5:
            self.word_list = self.word_list[1:]
        new_words = [self.generate_word() for _ in range(5 - len(self.word_list))]
        self.word_list = np.append(self.word_list, new_words)

    def get_word_list(self):
        self.update_word_list()
        return self.word_list
    
    def is_correct_word(self, word) -> bool:
        right_word = self.word_list[-3]
        return word == right_word
    
    def get_correct_word(self) -> str:
        return self.word_list[-3]
    
    def is_correctly_typed(self, word):
        length = len(word)
        if word == self.get_correct_word()[:length]:
            return True
        else:
            return False
    




    
    
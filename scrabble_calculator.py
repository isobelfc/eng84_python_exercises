# Scrabble class contains all necessary information
class Scrabble():
    def __init__(self):
        self.letter_score = {  # dictionary containing individual letter scores to reference
            "a": 1,
            "b": 3,
            "c": 3,
            "d": 2,
            "e": 1,
            "f": 4,
            "g": 2,
            "h": 4,
            "i": 1,
            "j": 8,
            "k": 5,
            "l": 1,
            "m": 3,
            "n": 1,
            "o": 1,
            "p": 3,
            "q": 10,
            "r": 1,
            "s": 1,
            "t": 1,
            "u": 1,
            "v": 4,
            "w": 4,
            "x": 8,
            "y": 4,
            "z": 10
        }

    def calculate_score(self, word):
        score = 0
        for letter in word:
            score += Scrabble().letter_score[letter]  # add the score of each letter to the total word score
        return score

# new object of Scrabble class
scoring = Scrabble()

# call calculate_score on a word and print the result
print(scoring.calculate_score("neptune"))

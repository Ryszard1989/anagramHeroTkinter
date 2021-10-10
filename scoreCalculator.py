def getLetterScores():
    letterScores = {'a': 1,
                    'b': 3,
                    'c': 3,
                    'd': 2,
                    'e': 1,
                    'f': 4,
                    'g': 2,
                    'h': 4,
                    'i': 1,
                    'j': 8,
                    'k': 5,
                    'l': 1,
                    'm': 3,
                    'n': 1,
                    'o': 1,
                    'p': 3,
                    'q': 10,
                    'r': 1,
                    's': 1,
                    't': 1,
                    'u': 1,
                    'v': 4,
                    'w': 4,
                    'x': 8,
                    'y': 4,
                    'z': 10
                    }
    return letterScores


def scoreCalculator(word, scrabbleTiles):
    letterScores = getLetterScores()
    score = 0
    scoreExplanation = "Score breakdown: "
    for char in word:
        scoreToAdd = letterScores[char]
        if scrabbleTiles.multiplier:
            if scrabbleTiles.doubleLetter == char:
                scoreToAdd = scoreToAdd * 2
                scoreExplanation += (char + ": " + str(letterScores[char]) + "(x2) , ")
            elif scrabbleTiles.tripleLetter == char:
                scoreToAdd = scoreToAdd * 3
                scoreExplanation += (char + ": " + str(letterScores[char]) + "(x3) , ")
            else:
                scoreExplanation += (char + ": " + str(letterScores[char]) + ", ")
        score += scoreToAdd
    if scrabbleTiles.multiplier:
        if scrabbleTiles.doubleWord:
            score = score * 2
            scoreExplanation += " (Word x2)"
        if scrabbleTiles.tripleWord:
            score = score * 3
            scoreExplanation += " (Word x3)"

    print(scoreExplanation)
    return score

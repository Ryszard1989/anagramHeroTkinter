import json

def isValidAnagram(proposedWord, generatedWord):
    sortedProposedWord = sorted(proposedWord)
    sortedGeneratedWord = sorted(generatedWord)
    flag = 0
    if set(sortedProposedWord).issubset(set(sortedGeneratedWord)):
        flag = 1
    if flag:
        return True
    else:
        print (proposedWord + " is not a valid anagram")
        return False

def isLongEnough(proposedWord):
    if len(proposedWord) < 2:
        print("Word must be at least 2 letters!")
        return False
    return True

class WordChecker:
    def __init__(self):
        with open('words_dictionary.json') as json_file:
            self.possibleWords = json.load(json_file)

    def checkWord(self, proposedWord, generatedWord):
        if isLongEnough(proposedWord) & \
                isValidAnagram(proposedWord, generatedWord) & \
                self.isValidWord(proposedWord):
            return True
        return False

    def isValidWord(self,proposedWord):
        if proposedWord in self.possibleWords:
            return True
        else:
            print (proposedWord + " is not a valid english word!")
            return False

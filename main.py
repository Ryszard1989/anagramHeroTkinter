import tkinter as tk
from wordGenerator import *
from wordChecker import *
from scoreCalculator import *

class GameManager:
    def __init__(self):
        #self.highScoreFP = "anagramHeroHighScores.csv"
        #self.highScoreTable = HighScoreTable(self.highScoreFP)
        self.currentScore = 0 #Reset for each user in a given session
        self.wordChecker = WordChecker()
        self.wordGenerator = WordGenerator()
        #self.gameLength = 5
        self.lblInstructions = None
        self.entry_userInput = None
        self.letterTileFrame = None
        self.lblTimer = None
        self.currentScoreWidget = None
        self.totalScoreWidget = None
        self.userEnteredWord = ""
        self.generatedTiles = ""
        self.remainingTime = 0
        #self.start = time.time()
        #self.currentTime = time.time()


class MainApplication(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.gameManager = GameManager()
        tk.Frame.__init__(self, self.master)
        self.configure_gui()
        self.create_widgets()
        self.countdown(60)

    def configure_gui(self):
        print("configure_gui")
        self.master.title("Anagram Hero")

    def create_widgets(self):
        print("create_widgets")
        self.setUpGameFrame()

    def setUpGameFrame(self):
        mainGameFrame = tk.Frame(
            master=self.master,
            relief=tk.RAISED,
            borderwidth=4
        )
        mainGameFrame.grid(row=0, column=0, padx=20, pady=0)
        self.setUpInstructions(mainGameFrame)
        self.setUpLetterTiles(mainGameFrame)
        self.setUpUserEntry(mainGameFrame)
        self.setUpTimerDisplay(mainGameFrame)
        self.setUpCurrentTurnResults(mainGameFrame)
        self.setUpTotalScoreDisplay(mainGameFrame)

    def setUpInstructions(self, mainGameFrame):
        lblInstructions = tk.Label(master=mainGameFrame,
                                    text="Make a word from: ",
                                    foreground="white", background="blue")
        lblInstructions.grid(row=0, column=1, sticky="nsew")
        self.lblInstructions = lblInstructions
        return lblInstructions

    def setUpLetterTiles(self, mainGameFrame):
        letterTileFrame = tk.Frame(
            master=mainGameFrame,
            relief=tk.RAISED,
            borderwidth=1
        )
        self.letterTileFrame = letterTileFrame
        letterTileFrame.grid(row=1, column=1, padx=20, pady=20)
        self.gameManager.generatedTiles = self.gameManager.wordGenerator.generateRandomWord(7)
        tiles = self.gameManager.generatedTiles.tiles
        tileIndex = 0
        for tile in tiles:
            lbl_letter = tk.Label(master=letterTileFrame,
                                  text=tile,
                                  foreground="black", background="yellow", borderwidth=4, relief=tk.SOLID)
            lbl_letter.config(width=4)
            lbl_letter.config(height=2)
            lbl_letter.config(font=("Courier", 28))
            lbl_letter.grid(row=1, column=tileIndex, sticky="nsew", padx=5, pady=5)
            tileIndex = tileIndex + 1
        return letterTileFrame

    def setUpUserEntry(self, mainGameFrame):
        userEntryFrame = tk.Frame(
            master=mainGameFrame,
            relief=tk.RAISED,
            borderwidth=1
        )
        userEntryFrame.grid(row=2, column=1, padx=20, pady=20)
        lbl_entry = tk.Label(master=userEntryFrame,
                             text="Enter word: ",
                             foreground="black", background="white",
                             borderwidth=0, relief=tk.SOLID)
        lbl_entry.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        entry_userInput = tk.Entry(width=50, master=userEntryFrame)
        self.entry_userInput = entry_userInput
        entry_userInput.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        btn_submitEntry = tk.Button(master=userEntryFrame, text="Submit", relief=tk.RAISED,
                                    command=self.processTurn,
                                    padx=10, pady=10, )
        # btn_submitEntry.bind("<Button-1>", self.cap)
        #btn_submitEntry.bind('<Return>', self.processTurn()) #TODO - Bind enter to submit
        btn_submitEntry.grid(row=0, column=2, sticky="nsew")
        return userEntryFrame

    def setUpTimerDisplay(self, mainGameFrame):
        lblTimer = tk.Label(master=mainGameFrame,
                                 text="0",
                                 foreground="black", background="white",
                                 borderwidth=0, relief=tk.SOLID)
        lblTimer.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        lblTimer.config(font=("Courier", 44))
        lblTimer.config(width='2')
        self.gameManager.lblTimer = lblTimer
        return lblTimer

    def setUpTotalScoreDisplay(self, mainGameFrame):
        lblTotalScore = tk.Label(master=mainGameFrame,
                             text="0",
                             foreground="black", background="white",
                             borderwidth=0, relief=tk.SOLID)
        lblTotalScore.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        lblTotalScore.config(font=("Courier", 44))
        lblTotalScore.config(width='2')
        self.gameManager.totalScoreWidget = lblTotalScore
        return lblTotalScore

    def setUpCurrentTurnResults(self, mainGameFrame):
        lblTurnScore = tk.Label(master=mainGameFrame,
                             text=" ",
                             foreground="black", background="white",
                             borderwidth=0, relief=tk.SOLID)
        lblTurnScore.config(font=("Courier", 44))
        lblTurnScore.config(width='2')
        lblTurnScore.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
        self.gameManager.currentScoreWidget = lblTurnScore
        return lblTurnScore
        #TODO - Work out how to get this to fill some more space to left, then do same for above with overall score on bottom left

    def processTurnEnter(self, event):
        self.processTurn()

    def processTurn(self):
        generatedTiles = self.gameManager.generatedTiles
        self.gameManager.userEnteredWord = self.entry_userInput.get()
        userEnteredWord = self.gameManager.userEnteredWord
        validWord = self.gameManager.wordChecker.checkWord(userEnteredWord, generatedTiles.tiles)
        if validWord:
            wordValue = scoreCalculator(userEnteredWord, generatedTiles)
            self.gameManager.currentScore += wordValue
            self.gameManager.currentScoreWidget['text'] = str("+" + str(wordValue))
            self.gameManager.totalScoreWidget['text'] = self.gameManager.currentScore

        self.refreshLetterTiles()
        self.entry_userInput.delete(0, "end")

    def refreshLetterTiles(self):
        self.gameManager.generatedTiles = self.gameManager.wordGenerator.generateRandomWord(7)
        print(self.gameManager.generatedTiles.tiles)
        tiles = self.gameManager.generatedTiles.tiles
        tile = 0
        for child in self.letterTileFrame.children.values():
            child['text'] = tiles[tile]
            tile = tile + 1

    def countdown(self, remaining=None):
        if remaining is not None:
            self.gameManager.remainingTime = remaining

        if self.gameManager.remainingTime <= 0:
            self.gameManager.lblTimer.configure(text="0!")
            self.entry_userInput.configure(state='disabled')
            self.lblInstructions.configure(text="Thank you for playing!", background="maroon")
        else:
            self.gameManager.lblTimer.configure(text="%d" % self.gameManager.remainingTime)
            self.gameManager.remainingTime = self.gameManager.remainingTime - 1
            self.after(1000, self.countdown)


if __name__ == '__main__':
    root = tk.Tk()
    main_app = MainApplication(root)
    root.bind('<Return>', main_app.processTurnEnter)
    root.mainloop()

# Imports, Tkiner for GUI, random for choosing word
import tkinter as GUI
from tkinter import messagebox
import random
# Word library used for game
word_library = [
    "cheese Snacks",
    "minecraft",
    "fortnite",
    "clown",
    "knife",
    "calculator",
    "coroner",
    "squid",
    "fishing",
    "Finland",
    "brother",
    "sister",
    "salt",
    "provide",
    "perceive",
    "player",
    "awful",
    "shareholder",
    "compliance",
    "matrix",
    "tempt",
    "context",
    "ferry",
    "register",
    "absence",
    "prey",
    "to",
    "dribble",
    "panel",
    "frank",
    "economist",
    "tip",
    "spy",
    "pressure",
    "revival",
    "absorb",
    "prevalence",
    "clock",
    "feast",
    "inside",
    "glass",
    "fling",
    "boom",
    "overall",
    "my",
    "offense",
    "flush",
    "outline",
    "conservation",
    "catalogue",
    "request",
    "reinforce",
]
# Hangman art credit: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
HANGMANPICS = ['''
       
       
       
       
       
       
=========''','''
      +
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



class hangman_game():
    class game_data():
        def __init__(self, word_chosen):
            self.chosen_word = word_chosen
            self.main_textvar = GUI.StringVar()
            self.word_length = len(self.chosen_word)
            self.main_textvar.set("-" * self.word_length)
            self.hang_textvar = GUI.StringVar()
            self.hang_textvar.set(HANGMANPICS[0])
            self.lives = len(HANGMANPICS) - 1
 
        def lose_life(self):
            self.lives -= 1
            print(str(self.lives))
            self.update_art()
                

        def update_art(self):
            self.hang_textvar.set(HANGMANPICS[len(HANGMANPICS) - 1 - self.lives])

    def exit_game(self):
        self.game_window.destroy()

    def init_window(self):
        self.game_window = GUI.Tk()
        self.game_window.geometry("200x210")
        self.game_window.resizable(False, False)
        self.game_window.title("Hang man")

    def clear_entry(self):
        self.text_entry.delete(0, "end")

    def check_gameover(self):
        if self.gamedata.lives == 0:
            print("Game Over!")
            messagebox.showwarning("GAME OVER", "You lose!")
            self.exit_game()

    def wrong_guess(self):
        print("Guess wrong")
        self.gamedata.lose_life()

    def replace_char(self, cur_string, new_char, index):
        return cur_string[:index] + new_char + cur_string[index + 1:]

    def check_victory(self):
        if self.gamedata.main_textvar.get() == self.gamedata.chosen_word:
            print("Game Victory")
            messagebox.showinfo("VICTORY!", "You win!")
            self.exit_game()

    def guess_character(self):
        current_char = ""
        current_guess = self.text_entry.get()
        if current_guess == "":
            print("Invalid guess")
            return
        else:
            current_char = current_guess[0]
        guess_length = len(current_char)
        _wordChosen = self.gamedata.chosen_word
        _currentString = self.gamedata.main_textvar.get()
        print("Guessed: " + current_char)
        if current_char.lower() in _wordChosen.lower():
            guess_count = 0
            index_of = _wordChosen.find(current_char)
            for i in range(len(_wordChosen)):
                if _wordChosen[i].lower() == current_char.lower():
                    _currentString = self.replace_char(_currentString, _wordChosen[i], i)
            print("Guess end: " + _currentString)
            self.gamedata.main_textvar.set(_currentString)
        else:
            #Wrong guess
            self.wrong_guess()
        self.check_victory()
        self.check_gameover()
        self.clear_entry()

    def init_elements(self):
        self.hang_label = GUI.Label(textvariable=self.gamedata.hang_textvar)
        self.word_label = GUI.Label(textvariable=self.gamedata.main_textvar)
        self.text_entry = GUI.Entry()
        self.submit_button = GUI.Button(text="Guess character", command=self.guess_character)
        self.hang_label.pack()
        self.word_label.pack()
        self.text_entry.pack()
        self.submit_button.pack()

    def __init__(self):
        self.init_window()
        self.gamedata = self.game_data(random.choice(word_library))
        self.init_elements()
        self.game_window.mainloop()



game_instance = hangman_game()
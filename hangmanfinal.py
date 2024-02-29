import random

class HangmanGame:
    def __init__(self, wordlist_filename):
        self.wordlist_filename = wordlist_filename
        self.word = self.get_random_word_from_wordlist()
        self.guessed_letters = []
        self.incorrect_guesses = 0

    def get_random_word_from_wordlist(self):
        try:
            with open(self.wordlist_filename, 'r') as file:
                wordlist = file.read().splitlines()
                wordlist = [word.strip() for word in wordlist]
                if not wordlist:
                    raise ValueError("Word list is empty")
                return random.choice(wordlist)
        except FileNotFoundError:
            print("Error: Word list file not found.")
        except ValueError as ve:
            print(f"Error: {ve}")
        return None

    def get_guess(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                return guess
            else:
                print("Please enter a single letter.")

    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter.lower() in self.guessed_letters or letter.upper() in self.guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        return displayed_word.strip()

    def draw_hanged_man(self):
        stages = [
            """
                -----
                |   |
                    |
                    |
                    |
              ______|______
            """,
            """
                -----
                |   |
                O   |
                    |
                    |
              ______|______
            """,
            """
                -----
                |   |
                O   |
                |   |
                    |
              ______|______
            """,
            """
                -----
                |   |
                O   |
               /|   |
                    |
              ______|______
            """,
            """
                -----
                |   |
                O   |
               /|\  |
                    |
              ______|______
            """,
            """
                -----
                |   |
                O   |
               /|\  |
               /    |
              ______|______
            """,
            """
                -----
                |   |
                O   |
               /|\  |
               / \  |
              ______|______
            """
        ]
        print(stages[self.incorrect_guesses])

    def is_game_over(self):
        if self.incorrect_guesses == 6:
            return True, "You lost! The word was " + self.word
        elif all(letter.lower() in self.guessed_letters or letter.upper() in self.guessed_letters for letter in self.word):
            return True, "Congratulations! You guessed the word: " + self.word
        else:
            return False, ""

    def play(self):
        while True:
            print(self.display_word())
            guess = self.get_guess()
            if guess not in self.guessed_letters:
                self.guessed_letters.append(guess)
                if guess.lower() not in self.word.lower():
                    self.incorrect_guesses += 1
                    self.draw_hanged_man()
            else:
                print("You already guessed that letter.")

            game_over, message = self.is_game_over()
            if game_over:
                print(message)
                break

def hangman():
    wordlist_filename = "hangman_wordlist.txt"
    game = HangmanGame(wordlist_filename)
    game.play()


hangman()

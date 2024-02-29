import random

def get_random_word_from_wordlist():
    try:
        with open("hangman_wordlist.txt", 'r') as file:
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

def get_guess():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Please enter a single letter.")

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter.lower() in guessed_letters or letter.upper() in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def draw_hanged_man(incorrect_guesses):
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
    print(stages[incorrect_guesses])

def is_game_over(word, guessed_letters, incorrect_guesses):
    if incorrect_guesses == 6:
        return True, "You lost! The word was " + word
    elif all(letter.lower() in guessed_letters or letter.upper() in guessed_letters for letter in word):
        return True, "Congratulations! You guessed the word: " + word
    else:
        return False, ""

def main():
    word = get_random_word_from_wordlist()
    if not word:
        return

    guessed_letters = []
    incorrect_guesses = 0

    while True:
        print(display_word(word, guessed_letters))
        guess = get_guess()
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            if guess.lower() not in word.lower():
                incorrect_guesses += 1
                draw_hanged_man(incorrect_guesses)
        else:
            print("Guessed that letter correct.")

        game_over, message = is_game_over(word, guessed_letters, incorrect_guesses)
        if game_over:
            print(message)
            break

if __name__ == "__main__":
    main()

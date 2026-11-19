import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman stage for the current mistakes and masked secret word."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: ", display_word)
    print("\n")


def play_game():
    """Runs the main Snowman Meltdown game loop."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check if all letters in the secret word have been guessed
        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations! You saved the snowman! The word was: {secret_word}")
            return

        guess = input("Guess a letter: ").lower().strip()

        if guess in secret_word:
            if guess not in guessed_letters:
                guessed_letters.append(guess)
        else:
            if guess not in guessed_letters:
                guessed_letters.append(guess)
                mistakes += 1

    # Final state when mistakes reach the limit
    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"Game over! The snowman melted! The secret word was: {secret_word}")
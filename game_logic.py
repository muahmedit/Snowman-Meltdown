import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, max_mistakes, secret_word, guessed_letters):
    """Displays the snowman stage, guessed letters, remaining tries, and masked word."""
    print(STAGES[mistakes])

    display_word = " ".join(
        letter if letter in guessed_letters else "_" for letter in secret_word
    )
    print(f"Word: {display_word}")

    wrong_guesses = sorted(letter for letter in guessed_letters if letter not in secret_word)
    guessed_display = ", ".join(sorted(guessed_letters)) if guessed_letters else "None"
    print(f"Guessed letters: {guessed_display}")
    print(f"Wrong guesses: {len(wrong_guesses)}/{max_mistakes}\n")


def get_valid_guess(guessed_letters):
    """Prompts until the user enters a single unguessed alphabetical letter."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input: please enter a single letter (a-z).")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue
        return guess


def play_round():
    """Runs a single round of Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("\nWelcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, max_mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations! You saved the snowman! The word was: {secret_word}")
            return

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print(f"Sorry, '{guess}' is not in the word.")
        else:
            print(f"Nice! '{guess}' is in the word.")

    display_game_state(mistakes, max_mistakes, secret_word, guessed_letters)
    print(f"Game over! The snowman melted! The secret word was: {secret_word}")


def play_game():
    """Runs the game with an optional replay loop."""
    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing Snowman Meltdown. Goodbye!")
            break
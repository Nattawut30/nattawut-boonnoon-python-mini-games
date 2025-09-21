# Hangman Words: Guess Game With Python By Nattawut Boonnoon (GitHub: @Nattawut30)

import random

# Dictionary storing hangman ASCII art for different stages (0 to 6 wrong guesses)
hangman_art = {
    0: ("   ", "   ", "   "),  # Empty stage
    1: (" o ", "   ", "   "),  # Head appears
    2: (" o ", " | ", "   "),  # Head and torso
    3: (" o ", "/| ", "   "),  # Head, torso, left arm
    4: (" o ", "/|\\", "   "),  # Head, torso, both arms
    5: (" o ", "/|\\", "/  "),  # Head, torso, arms, left leg
    6: (" o ", "/|\\", "/ \\")  # Full hangman (game over)
}

# Tuple of possible words for the game
words = ("LOVE", "HOPE", "HAPPINESS", "KINDNESS", "SUCCESS", "WONDERFUL", "JOY", "AMAZING", "FANTASTIC")

# Function to display the hangman based on the number of wrong guesses
def display_man(wrong_guesses):
    print("**********")  # Top border for visual clarity
    for line in hangman_art[wrong_guesses]:  # Print each line of the hangman art
        print(line)
    print("**********")  # Bottom border

# Function to display the current hint (e.g., "_ _ _ _" for "LOVE")
def display_hint(hint):
    print(" ".join(hint))  # Join hint list with spaces for readable output

# Function to display the answer (e.g., "L O V E")
def display_answer(answer):
    print(" ".join(answer))  # Join answer string with spaces for readable output

# Function to validate input against a set of valid options
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower().strip()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}.")

# Main game logic
def play_game():
    # Check if words list is empty
    if not words:
        print("No words available. Game cannot start.")
        return False

    # Select a random word and convert to lowercase
    answer = random.choice(words).lower()
    # Create a hint list with underscores for each letter
    hint = ["_"] * len(answer)
    # Track number of wrong guesses
    wrong_guesses = 0
    # Store guessed letters to prevent duplicates
    guessed_letters = set()

    # Main game loop
    while True:
        # Display current hangman state, hint, and guessed letters
        display_man(wrong_guesses)
        display_hint(hint)
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        # Get a valid single-letter guess
        guess = get_valid_input("Enter a letter: ", [chr(i) for i in range(97, 123)])

        # Check if letter was already guessed
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        # Add guess to guessed letters
        guessed_letters.add(guess)

        # Check if guess is in the answer
        if guess in answer:
            # Update hint with correct guess
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            # Increment wrong guesses if letter is not in answer
            wrong_guesses += 1

        # Check win condition: no underscores left in hint
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("VICTORY!")
            return True
        # Check loss condition: max wrong guesses reached
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("GAME OVER. TRY AGAIN!")
            return True

# Entry point to run the game
def main():
    while True:
        # Run a single game
        if not play_game():
            break  # Exit if game cannot start (e.g., empty word list)
        # Prompt for replay with validation
        play_again = get_valid_input("Play again? (y/n): ", ['y', 'n'])
        if play_again == 'n':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
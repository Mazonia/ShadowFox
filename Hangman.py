import random

words = ["python", "programming", "computer", "science", "machine", "learning", "artificial", "intelligence"]  # List of words
lives = 6  # Number of lives
display = []  # List to store displayed characters (underscores initially)

def generate_display(word):
    """Generates a display with underscores for each letter in the word."""
    for letter in word:
        display.append("_")

def update_display(guess, word):
    """Updates the display with the guessed letter if it's in the word."""
    global display
    for i, letter in enumerate(word):
        if guess == letter:
            display[i] = letter

def draw_hangman(lives_remaining):
    """Prints the visual representation of the hangman based on lives remaining."""
    stages = [  # ASCII art for different hangman stages
        """
          --------
          |      |
          |
          |
          |
          |
        ----------
        """,
        """
          --------
          |      |
          |      O
          |
          |
          |
        ----------
        """,
        """
          --------
          |      |
          |      O
          |      |
          |
          |
        ----------
        """,
        """
          --------
          |      |
          |      O
          |     /|\
          |
          |
        ----------
        """,
        """
          --------
          |      |
          |      O
          |     /|\
          |     /
          |
        ----------
        """,
        """
          --------
          |      |
          |      O
          |     /|\
          |     / \
          |
        ----------
        """
    ]
    print(stages[lives_remaining])

def get_hint(word):
    """Provides a hint (a random letter from the word) if lives are running low."""
    if lives <= 3:
        revealed_letters = "".join(letter for letter in display if letter != "_")
        for letter in word:
            if letter not in revealed_letters:
                return letter
        return "No more hints available!"

def main():
    """Main game loop."""
    global lives, display
    word = random.choice(words).lower()
    generate_display(word)

    while lives > 0 and "_" in display:
        print("\nYou have", lives, "lives remaining.")
        print(" ".join(display))

        guess = input("Guess a letter: ").lower()
        if guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Invalid input. Please enter a letter.")
            continue

        if guess in word:
            update_display(guess, word)
        else:
            lives -= 1
            print(guess, "is not in the word.")

        if lives <= 3:
            hint = get_hint(word)
            if hint != "No more hints available!":
                print("Hint:", hint)

        draw_hangman(lives)

    if lives == 0:
        print("You lost! The word was:", word)
    else:
        print("You won! The word was:", word)

if __name__ == "__main__":
    main()

import random

# List of predefined words
words = ["python", "java", "intern", "coding", "computer"]

# Randomly choose a word
secret_word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("🎯 Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

# Game loop
while wrong_guesses < max_wrong:
    # Display current word status
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())

    # Check win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly.")
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:
        print("✅ Good guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess! Remaining attempts:", max_wrong - wrong_guesses)

# Lose condition
if wrong_guesses == max_wrong:
    print("\n😢 You lost the game.")
    print("The word was:", secret_word)
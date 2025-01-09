def check_guess(guess, word):
    # Step 2: Convert the guess into lowercase
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input(word):
    while True:
        # Step 2: Ask the user to guess a letter
        guess = input("Guess a letter: ")

        # Step 3: Check if the guess is a single alphabetical character
        if guess.isalpha() and len(guess) == 1:
            # Step 3.1: Call check_guess to check if the guess is in the word
            check_guess(guess, word)
            break  # Exit the loop after a valid guess
        else:
            # Step 5: If the guess is invalid, print an error message
            print("Invalid letter. Please, enter a single alphabetical character.")


# Example word to guess
word = "python"

# Step 4: Outside the function, call ask_for_input to test your code
ask_for_input(word)

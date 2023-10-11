import string
import milestone_2

while True:
    guess = input("Enter a letter: ")  # User letter input
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in milestone_2.chosen_word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")
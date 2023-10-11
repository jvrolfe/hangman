import random   # Import the random module to select a random word from the created word list
import string   # Import the string module to check that a guess is a letter


hangman_word_list = ["Banana","Apple","Pear","Strawberry","Dragonfruit"]    # A list of words to select from
print(hangman_word_list)

chosen_word = random.choice(hangman_word_list)  # Using the random module with the choice method to randomly choose a word from the list and assining it to the variable word
print(chosen_word)

user_guess = input("Enter a letter: ")  # User letter input

if len(user_guess) == 1 and user_guess in string.ascii_letters:   # An if statement to check that the user input is a single letter
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
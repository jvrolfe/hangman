import random   # Import the random module to select a random word from the created word list
import string   # Import the string module to check that a guess is a letter


word_list = ["Banana","Apple","Pear","Strawberry","Dragonfruit"]    # a list of words to select from

print(word_list)

word = random.choice(word_list)  # Using the random module with the choice method to randomly choose a word from the list and assining it to the variable word

print(word)

guess = input("Enter a letter: ")  # User letter input

if len(guess) == 1 and guess in string.ascii_letters:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
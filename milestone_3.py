import string

while True:
    guess = input("Enter a letter: ")  # User letter input
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
import random

class Hangman():
    def __init__(self, word_list, num_lives=5):           
        self.word_list = word_list                      # A list of words
        self.word = random.choice(self.word_list)       # Chosen word
        self.num_letters = len(set(self.word))          # The number of unique letters in the chosen word
        self.num_lives = 5                              # Number of lives left. The initialised to 5 
        self.list_of_guesses = []                       # A list of previous guesses. This is initialised to an empty list
        self.word_guessed = ["_"] * len(self.word)      # Variable to hold the word and guesses
        
    def check_guess(self, guess):                           # A function to check if the guessed letter is the computer chosen word
        guess = guess.lower()                               # Converts the guess to lower case
        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                  self.word_guessed[self.word[letter]] = guess  
            self.num_letters -+ 1        
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        while True:  
            guess = input("Enter a letter: ")                                               # User letter input
            if len(guess) != 1 and guess.isalpha() == False:                                # Checks if guess does not = 1 and is not a letter
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:                                             # Checks if the guess is in the list of previous guesses
                print(f"You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
    

hangman_word_list = ["Banana","Apple","Pear","Strawberry","Dragonfruit"]                 
x = Hangman(hangman_word_list)


import random

class Hangman():

    '''
    This class is used to play the game of Hangman. 

    Parameters:
    word_list (list):  A list of words.
    num_lives (int): The number of remaining lives.
    
    Attributes: 
    word (str): Randomly chosen word.
    num_letters (int): The number of unique letters in word.     
    list_of_guesses (list): A list of letters already guessed. 
    word_guessed (list): a list the length of word where unguessed letters are represented by "_". 
    
    Methods:
    check_guess(guess): Checks if the guess is in the word.
    ask_for_input(): Asks the user for a letter. 
    '''
    def __init__(self, word_list, num_lives=5):           
        '''
        See help(Hangman) for accurate signature
        '''
        
        self.word_list = word_list                     # A list of words
        self.word = random.choice(self.word_list)      # Chosen word
        self.num_letters = len(set(self.word))         # The number of unique letters in the chosen word
        self.num_lives = num_lives                     # Number of lives left. The initialised to 5 
        self.list_of_guesses = []                      # A list of previous guesses. This is initialised to an empty list
        self.word_guessed = ["_"] * len(self.word)     # Variable to hold the word and guesses
        
        print(f"The word has {len(self.word_guessed)} letters in it.")      # informs the user of the number of letters in the word  
        print("  ".join(map(str, self.word_guessed)))                        # Prints the status of the word as a string
        pass

    def check_guess(self, guess):                           # A function to check if the guessed letter is the computer chosen word
        '''
        This function is used to check if the user input (guess) is in word, keep track of the number of lives left, 
        and update the state of the game with each guess. With each correct guess, "_" in word_guessed is 
        replaced with the letter. Each incorrect guess decreases the number of lives by 1. 

        Args:
            guess (str): The user input from ask_for_input() as a string.

        Returns:
        If the guess is in word:     
            str: "Good guess! {guess} is in the word." 
        If the guess is not in word:
            str: "Sorry, {guess} is not in the word. Try again." 
            str: "You have {self.num_lives} lives left."
        '''
        
        guess = guess.lower()
        lower_word = self.word.lower()                           # Converts the guess to lower case
        if guess in lower_word:
            print(f"Good guess! {guess} is in the word.")                     
            for index, letter in enumerate(lower_word):          # The word is enumerated as this indexes the word for ease of iteration       
                if letter == guess:                              
                    self.word_guessed[index] = guess             # If the guess is in the word, word_guess is updated to include the uess at the correct index      
            self.num_letters -= 1                                
        else:
            self.num_lives -= 1
            if self.num_lives > 0:
                print(f"Sorry, {guess} is not in the word. Try again.")
                print(f"You have {self.num_lives} lives left.")
            else:
                print(f"Sorry, {guess} is not in the word.")
                print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        '''
        This function repeatedly asks the user for a single alphabetical character, checks if it's a valid guess,
        and calls the check_guess method to update the game state. It also keeps track of previous guesses. 

        Returns:
        If the guess is a single, alphabetic character:
            guess: The user input stored as an attribute parsed to check_guess().        
        If the guess is a single, alphabetic character and previously guessed:
            str: "You already tried that letter!"
        If the guess is NOT a single, alphabetic character:
            str: "Invalid letter. Please, enter a single alphabetical character."
            
        '''
        
        while True:  
            guess = input("Enter a letter: ")                                               # User letter input
            if len(guess) != 1 or not guess.isalpha():                                      # Checks if guess does not = 1 and is not a letter
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:                                             # Checks if the guess is in the list of previous guesses
                print(f"You already tried that letter!")
            else:                
                self.check_guess(guess)                
                print("  ".join(map(str, self.word_guessed)))                                # Prints the status of the word as a string
                self.list_of_guesses.append(guess)                                          # The list of previous guesses is updated
            if self.num_lives <= 0 or self.num_letters == 0:                                # Breaks the while loop if lives or num_letters = 0
                break   
          
    

def play_game(word_list):
    '''
    This function is used to play the game of Hangman. The word_list is passed as an argument, and an instance of the Hangman class is created within the function. 
    Whilst the number of lives and unique letters left to guess in the word are > 0, this function whill repeatedly ask for the user input. 
    When either of these variables = 0, the loop is broken and the game ends. 

        Args:
            word_list (list): A list of words.

        Returns:
        If num_lives = 0:     
            str: "You lost!" 
        If the user guesses the word correctly:
            str: "Congratulations. You won the game!" 
    '''
    num_lives = 5 
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:                             # Condition for losing the game
            print(f"You lost! The word was {game.word}.")
            break
        elif game.num_letters > 0:                          # Condition to continue the game
            game.ask_for_input()
        else:                                               # Condition to win the game
            print(f"Congratulations. You won the game!")
            break

if __name__ == "__main__":  
    word_list = ["Banana","Apple","Pear","Strawberry","Dragonfruit"]
    play_game(word_list)                    # Testing that the above code works
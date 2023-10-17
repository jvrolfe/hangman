import random
import milestone_2

class Hangman():

    '''
    This class is used to play the game of Hangman. 

    Attributes: 
    word_list (list):  A lsit of words.
    word (str): Randomly chosen word.
    num_letters (int): The number of unique letters in word.
    num_lives (int): The number of remaining lives. 
    list_of_guesses (list): A list of letters already guessed. 
    word_guessed (list): a list the length of word where unguessed letters are represented by "_". 
    '''
    def __init__(self, word_list, num_lives=5):           
        '''
        See help(Hangman) for accurate signature
        '''
        
        self.word_list = word_list                      # A list of words
        self.word = random.choice(self.word_list)      # Chosen word
        self.num_letters = len(set(self.word))          # The number of unique letters in the chosen word
        self.num_lives = num_lives                              # Number of lives left. The initialised to 5 
        self.list_of_guesses = []                       # A list of previous guesses. This is initialised to an empty list
        self.word_guessed = ["_"] * len(self.word)      # Variable to hold the word and guesses
        
    def check_guess(self, guess: str):                           # A function to check if the guessed letter is the computer chosen word
        '''
        This function is used to check if the user input (guess) is in word, keep track of the number of lives left, 
        and update the state of the game with each guess.

        Args:
            guess: The user input from ask_for_input() as a string.

        Returns:
        If the guess is in word:     
            str: "Good guess! {guess} is in the word." 
        If the uess is not in word:
            str: "Sorry, {guess} is not in the word. Try again." 
            str: "You have {self.num_lives} lives left."
        '''
        
        guess = guess.lower()
        lower_word = self.word.lower()                              # Converts the guess to lower case
        if guess in lower_word:
            print(f"Good guess! {guess} is in the word.")                     
            for index, letter in enumerate(lower_word):               
                if letter == guess:                    
                    self.word_guessed[index] = guess                   
            self.num_letters -= 1        
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
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
                print(f"Current word: {self.word_guessed}")
                self.list_of_guesses.append(guess)
            if self.num_lives <= 0 or self.num_letters == 0:
                break   
          
    

def play_game(word_list):
    num_lives = 5 
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f"You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print(f"Congratulations. You won the game!")
            break

      
play_game(milestone_2.hangman_word_list)
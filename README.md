# Hangman

In this project, I have created my version of the [Hangman](<https://en.wikipedia.org/wiki/Hangman_(game)>) game in Python as part of the AiCore Data Analytics pathway content. Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. The user must guess the word one letter at a time. If a letter in the word is guessed correctly, it is filled in. Each incorrect guess draws a new part of the man, and if enough incorrect guesses are made, the man is hanged. 

The motivation for this project is to demonstrate my understanding of Python based on the learning content and self-learning up to this point in the course. 

## Requirements

- Fork this repo
- Clone this repo
- Python3

## Usage
How the program works:

Step One: Firstly, this program randomly selects a word from a given list.

Step Two: The _ask_for_input()_ function is called. This function asks the user to input a single letter and then passes this guess into the __check_guess()__ function, which checks if the guessed letter is in the chosen word. 

Step Three:


## File Structure: 
This program is separated into X AMOUNT of different modules. 

**milestone_2.py**: Within this module two key variables are defined. 
- __hangman_word_list__: Defines the list of words the computer can randomly choose from.
- __chosen_word__: Using the choice function from the random module, the computer chooses a word from the __hangman_word_list__.

If you want to see the list of words and the chosen word, run the milestone_2 code directly.

**milestone_3.py**: Within this module, the user inputs a single letter guess. The milestone_2 module is imported, and the users guess compared with the chosen word. 
- __

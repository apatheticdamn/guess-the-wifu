from wifu_list import wifu_list 
from random import choice 

wifu = choice(wifu_list).lower() # one wifu from wifu list each time you run the code
wifu_characters = set(wifu) # set of unique characters
length = len(wifu) 

print("The wifu's name is {} characters long...".format(length))

correct_guesses = set()
wrong_guesses = set()

while correct_guesses != set(wifu_characters): # continue until all the characters are guessed
    display = "".join(letter if letter in correct_guesses else "_" for letter in wifu)
    print(f"Current progress: {display}")
    
    guess = input("Guess the wifu: ").lower()
    
    if guess.isalpha() and len(guess) == 1: # checks if the guess is single alphabetical character or not
        if guess in correct_guesses or guess in wrong_guesses:
            print("Hey, you've already guessed that character")
            
        elif guess in wifu_characters: # checks if the guess is correct and updates the correct_guesses set
            correct_guesses.add(guess)
            
        else: # if the guess is wrong the wrong guesses set will be updated
            wrong_guesses.add(guess)
            print("Sorry wrong guess, please try again!")
    else: # if the user enters a number or multiple characters
        print("Please enter a single valid character")

print("Yay, you've guessed the wifu {}.".format(wifu))


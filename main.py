from wifu_list import wifu_list
from random import choice

wifu = choice(wifu_list).lower()
wifu_characters = set(wifu)
length = len(wifu)
print("The wifu's name is {} characters long...".format(length))
correct_guesses = set()
wrong_guesses = set()

while correct_guesses != set(wifu_characters):
    display = "".join(letter if letter in correct_guesses else "_" for letter in wifu)
    print(f"Current progress: {display}")
    guess = input("Guess the wifu: ").lower()
    if guess.isalpha() and len(guess) == 1:
        if guess in correct_guesses or guess in wrong_guesses:
            print("Hey, you've already guessed that character")
        elif guess in wifu_characters:
            correct_guesses.add(guess)
        else:
            wrong_guesses.add(guess)
            print("Sorry wrong guess, please try again!")
    else:
        print("Please enter a single valid character")

print("Yay, you've guessed the wifu {}.".format(wifu))


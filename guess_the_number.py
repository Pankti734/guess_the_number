#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

print(logo)
print("Welcome to the number guessing game")
print("I am thinking of a number between 1 and 100 ")

choosen_word = random.randint(1, 100)
print(choosen_word)

# while diff1:
# 	attempts=10
# 	for i in range(1,10):
# 		attempts-=1
# 		print(f"You {attempts}have attempts remaining to guess the number.")


def easy():
    attempts = 10
    for i in range(1, 10):
        guess = input("Make a guess:")
        if guess == choosen_word:
            print("You won")
        else:
            if guess >= choosen_word:
                print("Too high")
            elif guess < choosen_word:
                print("Too low")
            attempts -= 1
            print(
                f"You have {attempts} attempts remaining to guess the number.")


diff = input("Choose a difficulty.Type 'easy' or 'hard'\n")
if diff == "easy":
    easy()

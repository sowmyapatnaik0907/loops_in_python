
import random

secret_number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    attempts -= 1

    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break
else:
    print("Better luck next time!")
    print("The correct number was:", secret_number)

import random

limit = int(input("I will now choose a number between 1 and x and you will have to guess it. Please state x: "))

random_number = random.randint(1,limit)

guess = int(input("What is you guess: "))

while guess != random_number :
    if guess < random_number :
        print("Your guess is too low.")
        guess = int(input("Please guess again: "))
    elif guess > random_number :
        print("Your guess is too high.")
        guess = int(input("Please guess again: "))

print("Your guess is correct. You win!")

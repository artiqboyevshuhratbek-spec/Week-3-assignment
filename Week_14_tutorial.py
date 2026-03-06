import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    attempts = 5
    
    print("I'm thinking of a number between 1 and 20.")
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}/{attempts}. Enter your guess: "))
        
        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print("You got it!")
            return 
    print(f"Game Over! The correct number was {secret_number}.")
guess_the_number()
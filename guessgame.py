import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("Welcome to the Number Guessing Game!")
    print(f"Guess the number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess}!")
            return

        attempts += 1
        attempts_left = max_attempts - attempts
        if attempts_left > 0:
            print(f"Attempts left: {attempts_left}")
        else:
            print("Out of attempts. Game over!")
            print(f"The number was: {number_to_guess}")

number_guessing_game()
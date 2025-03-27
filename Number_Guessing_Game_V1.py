import random

def number_guessing_game():
    print(
        "Welcome to the Number Guessing Game!\n"
        "I've chosen a random number between 1 and 9. Can you guess it?\n"
        "(Type 'q' to quit at any time.)"
    )

    number = random.randint(1, 9)
    attempts = 0

    while True:
        guess = input("Your guess: ").strip().lower()

        if guess == 'q':
            print(f"Game ended. The number was {number}.")
            break

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a number between 1-9 or 'q' to quit.")
            continue

        attempts += 1

        if guess < 1 or guess > 9:
            print("Please enter a number between 1 and 9.")
        elif guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts!")
            break

if __name__ == "__main__":
    number_guessing_game()
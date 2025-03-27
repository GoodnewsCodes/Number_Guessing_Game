import random

print("Welcome to my Number Guessing Game"
"\n I've chosen a random number between 1 to 9, try guessing it")

number = random.randint(1, 9)
guess = None

while guess != number:
    guess = input(" ")
    if guess == "q" or guess == "Q":
        break
    guess = int(guess)

    if guess > number:
        print("That's higher, Try again"
            "\n Type 'q' if you want to end the game:")

    elif guess < number:
        print("Thats lower than the number, Try again"
              "\n Type 'q' if you want to end the game:")
    
    else:
        number = str(number)
        print("Wow, You guesseed right! The number was indeed " + number + ".")
        break
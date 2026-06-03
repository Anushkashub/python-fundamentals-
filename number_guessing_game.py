import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number : "))

    if guess == secret_number:
        print("Congratulations! You guessed it correctly.")
        break

    elif guess < secret_number:
        print("Too Low! Try again.")

    else:
        print("Too High! Try again.")

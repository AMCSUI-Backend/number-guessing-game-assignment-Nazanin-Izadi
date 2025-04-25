import random

def game():
    right_number = random.randint(1, 100)
    guess_counter = 0
    max_guesses = 8
    print("Welcome To The Number Guessing Gameeee")
    while guess_counter < max_guesses:
        guess_input = input("please Enter your number between 1 and 100: ")
        if guess_input.isdigit():
            user_guess = int(guess_input)
            guess_counter += 1
            if user_guess < right_number:
                print("Too low!")
            elif user_guess > right_number:
                print("Too high!")
            else:
                print("Congratulations! You guessed it!")
                print("Guessess:", guess_counter)
                return
        else:
            print("oops it's not a number! Please enter a number.")

    print("Your chances is out! The number was", right_number)

while True:
    game()
    repeat = input("Do you want to play again? (yes/no): ")
    if repeat != "yes":
        print("I Hope You Enjoyed it :)")
        break

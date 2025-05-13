import random

print("Welcome to the Number Guessing Game! 🎯")

while True:
    number_to_guess = random.randint(1, 10)
    attempts = 0
    
    while True:
        guess = input("Guess a number between 1 and 10: ")

        if not guess.isdigit():
            print("Please enter a valid number!")
            continue

        guess = int(guess)
        attempts += 1

        if guess == number_to_guess:
            print(f"Congratulations! 🎉 You guessed it in {attempts} attempts.")
            break
        elif guess < number_to_guess:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break

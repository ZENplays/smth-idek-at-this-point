import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Guess the num fro 1-100")

    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("higher than ", guess)
            elif guess > number_to_guess:
                print("lower than", guess)
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()

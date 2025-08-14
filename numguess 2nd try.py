import random

difficulties = ["Easy", "Medium", "Hard"]


def set_difficulity():
    print("1-Easy: number from 1 to 10")
    print("2-Medium: number from 1 to 100")
    print("3-Hard: number from 1 to 1000")

    while True:
        difficulty = input("Please select a difficulty (1-3): ")

        try:
            difficulty = int(difficulty)
            if difficulty in [1, 2, 3]:
                return difficulty
            else:
                print("Please select a valid number")
        except ValueError:
            difficulty = input("please select a valid number (1-3): ")


def guess_func():
    while True:
        guess = input(f"Please select a number from (1-{10**difficulty}): ")

        try:
            guess = int(guess)
            if guess < 1 or guess > 10**difficulty:
                print(f"Please guess a valid Number (1-{10**difficulty})")
            else:
                return guess
        except ValueError:
            print("Please select a valid number")


is_running = True
while is_running:
    difficulty = set_difficulity()
    print(f"You selected {difficulties[difficulty - 1]} difficulty")
    answer = random.randint(1, 10**difficulty)
    no_of_guesses = 0
    while True:
        guess = guess_func()

        if guess > answer:
            print("Try a smaller number")
            no_of_guesses += 1
        elif guess < answer:
            print("Try a bigger number")
            no_of_guesses += 1
        else:
            print("Correct!")
            no_of_guesses += 1
            print(f"You guessed the correct answer in {no_of_guesses} guesses")
            break

    is_running = input('Press "Enter" to quit / any button to play again: ')

import random

# Constants
LOWER_RANGE_NUMBER = 0
UPPER_RANGE_NUMBER = 100

def guessing_game():
    """
    A method to execute the guessing game
    """
    number = random.randint(LOWER_RANGE_NUMBER, UPPER_RANGE_NUMBER)
    print(f'Backdoor answer: {number}')
    while True:
        user_guess = input(f'Welcome, guess a number between {LOWER_RANGE_NUMBER} to {UPPER_RANGE_NUMBER}: ')
        user_guess = int(user_guess)
        if user_guess < number:
            print(f'Your guess of {user_guess} is too low, guess again.')
        elif user_guess > number:
            print(f'Your guess of {user_guess} is too high, guess again.')
        else:
            print(f'Your guess of {user_guess} is just right!')
            break


def main():
    guessing_game()


if __name__ == '__main__':
    main()
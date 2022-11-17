from num_guess_game_art import logo
from random import randint

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
chosen_number = randint(1, 100)

not_chosen_difficulty = True


def chosen_difficulty_and_num_of_guesses():
    global not_chosen_difficulty
    while not_chosen_difficulty:
        difficulty_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty_input == 'easy':
            guesses = 10
            not_chosen_difficulty = False
            return guesses
        elif difficulty_input == 'hard':
            guesses = 5
            not_chosen_difficulty = False
            return guesses
        else:
            not_chosen_difficulty = True


num_guesses = chosen_difficulty_and_num_of_guesses()
guess = True

while num_guesses >= 0:
    if num_guesses == 0:
        print(f"You lose! The number was {chosen_number}.")
        break
    else:
        print(f'You have {num_guesses} attempts remaining to guess the number.')
        guess_attempt_num = input('Make a guess: ')
        if guess_attempt_num.isdigit():
            guess_attempt_num = int(guess_attempt_num)
            if guess_attempt_num > chosen_number:
                num_guesses -= 1
                print("Too high. \nGuess again.")
            elif guess_attempt_num < chosen_number:
                num_guesses -= 1
                print("Too low. \nGuess again.")
            elif guess_attempt_num == chosen_number:
                print("You win!")
                break


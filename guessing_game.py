"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game():
    high_score = 100
    play_again = True

    while play_again:
        if high_score == 100:
            print(f"There is no high score yet. Play the game once to set the high score!")
        elif high_score != 100:
            print(f"The high score is {high_score}. See if you can beat it!")
        print()
        print("""Welcome to the number guessing game! In this game, you will have to guess a number between 1 and 10.
        If you guess incorrectly, you will be given a hint if the number is higher or lower than what you guessed.
        Try to guess the number in as few attempts as possible! Happy guessing!""")
        print()
        num_to_guess = random.randrange(1, 11)
        num_tries = 0
        playing = True
        while playing:
            user_guess = 0
            while user_guess < 1 or user_guess > 10:
                user_guess = int(input("Please guess a number between 1 and 10: "))
                num_tries += 1
            if user_guess == num_to_guess:
                print(f"You did it! You guessed the number, which was {num_to_guess}! It took you {num_tries} tries to guess it!")
                break
            elif user_guess < num_to_guess:
                print(f"Your guess {user_guess} is lower than the number to guess!")
            elif user_guess > num_to_guess:
                print(f"Your guess {user_guess} is higher than the number to guess!")
            print()
        if num_tries < high_score:
            high_score = num_tries
        while True:
            want_play_again = input("Would you like to play again? Enter y for yes and n for no: ")
            if want_play_again == 'y' or want_play_again == 'n':
                break
        if want_play_again == 'y':
            play_again = True
        elif want_play_again == 'n':
            play_again = False
    print("Thanks for playing!")


start_game()

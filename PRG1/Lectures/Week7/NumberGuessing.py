#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-Short-Identifier: MIT
# (c) 2019 Rifa I. Achrinza
# This code is licensed under MIT license (See LICENSE.txt for details)

import random

__author__ = "Rifa I. Achrinza"
__copyright__ = "Copyright 2019, Rifa I. Achrinza"
__credits__ = ["Rifa I. Achrinza"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Rifa I. Achrinza"
__email__ = "rifa@achrinza.com"
__status__ = "Production"

def main() -> None:
    # Assign 'global' variables
    rand_num_min = 1                                      # Generated random number minimum value (inclusive)
    rand_num_max = 100                                    # Generated random number maximum value (inclusive)
    attempt_count = 1                                     # The nth attempt counter
    attempt_count_max = 5                                 # Maximum number of attempts
    rand_num = random.randint(rand_num_min, rand_num_max) # Generate the random number to guess

    print("Welcome to Number Guessing Game")
    while True:
        # Limit number of attempts.
        # If max attempts reached, immediately stop the game.
        # Use more-than instead of equals-to to prevent accidental increments beyond 1
        # (e.g. attemptCount skips attemptCountMax due to an increment by 2)
        if attempt_count > attempt_count_max:
            break

        # Keep asking for the user's response until a valid number is entered.
        # While loop to keep prompting
        # Try-except to catch non-int inputs and prevent the program from throwing an error and exiting
        attempt_response = None
        while attempt_response is None:
            try:
                attempt_response = int(input("Try {}: Enter a number between {} and {} (or -1 to end) :".format(
                    attempt_count, rand_num_min, rand_num_max
                )))
            except ValueError:
                continue

        # Check if the user wants to quit the game prematurely
        # If so, break out of the loop
        if attempt_response == -1:
            break

        # Check if the user got the correct answer
        elif attempt_response == rand_num:
            print("Bingo, you've got it right!")

        # Check if the user's answer is too low
        elif attempt_response < rand_num:
            print("{} is too low".format(attempt_response))

        # If all other conditions fail, the user's answer is naturally too high
        else:
            print("{} is too high".format(attempt_response))

        # Increment our attempt counter after each attempt
        attempt_count += 1

    # Print the exit text after the game has ended regardless of the game state
    # (e.g. Regardless if the user won, lost or quit)
    # Newline special character to make output identical to test case scenario from question
    print("\nBye-bye!")

# Check if the Python program is run as a standalone program and not as an imported module
# If so, run the program. Otherwise, don't run the program.
if __name__ == "__main__":
    main()

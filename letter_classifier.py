#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Apr. 14, 2025
# This program determines whether a letter of the English
# alphabet is a consonant, vowel, or semivowel. It also
# allows the user to find extra information about a particular
# letter by displaying phonetic symbols and examples if desired.

# Import the constants module to use constants.
import constants

# Define the main function.
def main():
    # Construct an infinite loop.
    while True:
        # Get the desired letter from the user.
        user_letter = input("Enter a letter from a-z or A-Z: ")

        # Checks if the lowercase letter entered is a 
        # letter of the English alphabet.
        if user_letter.lower() in constants.ENGLISH_LETTERS:
            # Break the infinite loop.
            break
        # Otherwise, they did not enter a valid letter.
        else:
            # Display to the user that they must
            # enter a valid letter of the English alphabet.
            print(f"\n{user_letter} is not a valid letter of the English alphabet. "
            "Please enter a letter from a-z or A-Z.\n")

    # Construct an infinite while loop.
    while True:
        # Get the desired display type from the user.
        user_display_type = input("\nEnter a display type for the letter "
        "(simple = straightforward answer, complex = sophisticated answer): ")

        # Check if simple or complex was the entered display type.
        if ((user_display_type.lower() == "simple") or (user_display_type.lower() == "complex")):
            # Break the infinite loop.
            break
        # Otherwise, they did not enter a valid display type.
        else:
            # Display to the user that they must enter a valid choice.
            print(f"{user_display_type} is not a valid choice. Please "
            "enter either simple or complex for the display type.")

                    
    








# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()

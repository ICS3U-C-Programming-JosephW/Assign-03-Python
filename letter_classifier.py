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
    # Construct an infinite while loop for the letter input.
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

    # Construct an infinite while loop for the display input.
    while True:
        # Get the desired display type from the user.
        user_display_type = input("\nEnter a display type for the letter "
        "(simple = straightforward answer, complex = sophisticated answer): ")

        # Check if simple or complex was the entered display type.
        if ((user_display_type.lower() == "simple") 
        or (user_display_type.lower() == "complex")):
            # Break the infinite loop.
            break
        # Otherwise, they did not enter a valid display type.
        else:
            # Display to the user that they must enter a valid choice.
            print(f"{user_display_type} is not a valid choice. Please "
            "enter either simple or complex for the display type.")

    # Construct an infinite while loop 
    # for the phonetic symbol choice input.
    while True:
        # Get the user's choice of displaying a 
        # phonetic symbol for their desired letter.
        show_phonetic_symbol_str = input("\nDo you want a phonetic symbol to be "
        "displayed for the sound your letter makes?\n Enter 0 for no or 1 for yes: ")

        # Try to validate and proceed with the 
        # user's choice for a phonetic symbol.
        try:
            # Attempt to convert the entered string into an integer.
            show_phonetic_symbol_int = int(show_phonetic_symbol_str)

            # Check if the user entered 0 for no or 1 for yes.
            if ((show_phonetic_symbol_int == 0) or 
            (show_phonetic_symbol_int == 1)):
                # Construct a nested infinite while loop 
                # for the phonetic example choice input.
                while True:
                    # Get the user's choice of displaying a 
                    # phonetic symbol for their desired letter.
                    show_phonetic_example_str = input("\nDo you want a phonetic "
                    "word to be displayed for an example relating to your chosen "
                    "letter?\n Enter 0 for no or 1 for yes: ")
                    
                    # Try to validate and proceed with the 
                    # user's choice for a phonetic example. 
                    try:
                        # Attempt to convert the entered string into an integer.
                        show_phonetic_example_int = int(show_phonetic_example_str)

                        # Check if the user entered 0 for no 
                        # or 1 for yes for the phonetic example.
                        if ((show_phonetic_example_int == 0) or 
                        (show_phonetic_example_int == 1)):
                            # Break the inner infinite while loop.
                            break
                        # Otherwise, the user entered an integer out of range
                        # for the example choices.
                        else:
                            # Display to the user that they must enter 0 for no
                            # or 1 for yes for the phonetic example.
                            print(f"{show_phonetic_example_int} is out of "
                            "range for choices. Please enter either "
                            "0 for no or 1 for yes.")
                    # Runs if int() could not convert the user's string 
                    # input into an integer for the example choice.
                    except ValueError:
                        # Display to the user that they need to enter
                        # a valid integer for the example choice.
                        print(f"{show_phonetic_example_str} is not a valid integer. "
                        "Please enter a valid integer.")
            # Otherwise, the user entered an integer out of range
            # for the symbol choices.
            else:
                # Display to the user that they must enter 0 for no
                # or 1 for yes for the phonetic symbol.
                print(f"{show_phonetic_symbol_int} is out of range for choices. "
                "Please enter either 0 for no or 1 for yes.")
        except ValueError:
            # Runs if int() could not convert the user's string 
            # input into an integer for the example choice.
            pass

                    
    
# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()

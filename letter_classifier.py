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
        user_letter = input("Enter a letter from a-z or A-Z: \n")

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
        "(simple = straightforward answer, complex = sophisticated answer): \n")

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
        "displayed for the sound your letter makes?\nEnter 0 for no or 1 for yes: ")

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
                    "letter?\nEnter 0 for no or 1 for yes: ")
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
                # Break the outer infinite while loop.
                break
            # Otherwise, the user entered an integer out of range
            # for the symbol choices.
            else:
                # Display to the user that they must enter 0 for no
                # or 1 for yes for the phonetic symbol.
                print(f"{show_phonetic_symbol_int} is out of range for choices. "
                "Please enter either 0 for no or 1 for yes.")
        # Runs if int() could not convert the user's string 
        # input into an integer for the symbol choice.
        except ValueError:
            # Display to the user that they need to enter
            # a valid integer for the symbol choice.
            print(f"{show_phonetic_symbol_str} is not a valid integer. " 
            "Please enter a valid integer.")

    # Determine the place of the lowercase chosen letter in the 
    # English alphabet by finding its index in the array of English
    # letters and adding it by 1.
    letter_place = constants.ENGLISH_LETTERS.index(user_letter.lower()) + 1

    # Check if the letter place ends in 1 and does not end in 11.
    if ((letter_place % 10 == 1) and (letter_place % 100 != 11)):
        # Set the letter place to "st."
        letter_place_suffix = "st"
    # Otherwise, check if the letter place ends in 2 and does not end in 12.
    elif ((letter_place % 10 == 2) and (letter_place % 100 != 12)):
        # Set the letter place to "nd."
        letter_place_suffix = "nd"
    # Otherwise, check if the letter place ends in 3 and does not end in 13.
    elif ((letter_place % 10 == 3) and (letter_place % 100 != 13)):
        # Set the letter place to "rd."
        letter_place_suffix = "rd"
    # Otherwise, it has to be "th." That is the only other suffix.
    else:
        # Set the letter place to "th."
        letter_place_suffix = "th"

    # Match the user's chosen letter in lowercase with cases 
    # to determine if it is a consonant, vowel, or semivowel.
    match user_letter.lower():
        # The consonant case when the user display type in lowercase is simple.
        case ('b' | 'c' | 'd' | 'f' | 'g' | 'h' | 'j' | 'k' 
        | 'l' | 'm' | 'n' | 'p' | 'q' | 'r' | 's' | 't' 
        | 'v' | 'x' | 'z') if user_display_type.lower() == "simple":
            # Display to the user that their 
            # letter in uppercase is a consonant.
            print(f"The letter {user_letter.upper()} is a consonant.")

        # The consonant case when the user display type in lowercase is complex.
        case ('b' | 'c' | 'd' | 'f' | 'g' | 'h' | 'j' | 'k' 
        | 'l' | 'm' | 'n' | 'p' | 'q' | 'r' | 's' | 't' 
        | 'v' | 'x' | 'z') if user_display_type.lower() == "complex":
            # Display to the user that their letter in uppercase
            # is a consonant with more information.
            print(f"The letter {user_letter.upper()}, the {letter_place}"
            f"{letter_place_suffix} letter of the English alphabet, "
            "is a consonant. Consonants are speech sounds made with "
            "some or complete closure of the vocal tract.")

        # The vowel case when the user display type in lowercase is simple.
        case ('a' | 'e' | 'i' | 'o' | 'u') if user_display_type.lower() == "simple":
            # Display to the user that their 
            # letter in uppercase is a vowel.
            print(f"The letter {user_letter.upper()} is a vowel.")

        # The vowel case when the user display type in lowercase is complex.
        case ('a' | 'e' | 'i' | 'o' | 'u') if user_display_type.lower() == "complex":
            # Display to the user that their letter in 
            # uppercase is a vowel with more information.
            print(f"The letter {user_letter.upper()}, the {letter_place}"
            f"{letter_place_suffix} letter of the English alphabet, "
            "is a vowel. Vowels are speech sounds made with "
            "little to no closure of the vocal tract.")

        # The semivowel case when the user display type in lowercase is simple.
        case ('w' | 'y') if user_display_type == "simple":
            # Display to the user that their 
            # letter in uppercase is a semivowel.
            print(f"The letter {user_letter.upper()} is a semivowel.")
        
        # The semivowel case when the user display type in lowercase is complex.
        case ('w' | 'y') if user_display_type == "simple":
            # Display to the user that their letter in 
            # uppercase is a semivowel with more information.
            print(f"The letter {user_letter.upper()}, the {letter_place}"
            f"{letter_place_suffix} letter of the English alphabet, "
            "is a semivowel. Semivowels are special speech sounds that "
            "share some characteristics of a vowel and a consonant.")

    # Set the corresponding index to the place of the letter
    # subtracted by one to revert back to array indexes.
    corresponding_index = letter_place - 1

    # Check if the user wanted a phonetic symbol 
    # to be displayed based on the letter.
    if show_phonetic_symbol_int == 1:
        # Set the corresponding symbol to the corresponding index
        # of the phonetic symbol array.
        corresponding_phonetic_symbol = constants.PHONETIC_SYMBOLS[corresponding_index]

        # Display to the user the phonetic symbol for the letter when said alone.
        print(f"The phonetic notation for the letter {user_letter.upper()} " 
        f"when said in isolation is {corresponding_phonetic_symbol}.")
    
    # Check if the user wanted a phonetic example 
    # word to be displayed based on the letter.
    if show_phonetic_example_int == 1:
        # Set the corresponding symbol to the corresponding index
        # of the example words array.
        corresponding_example_word = constants.EXAMPLE_WORDS[corresponding_index]

        # Display to the user a word that uses 
        # the letter they chose in uppercase.
        print("One example of a word that uses the letter "
        f"{user_letter.upper()} is {corresponding_example_word}.")

    # Finally, thank the user for using this program.
    print("Thanks for using this program!") 

# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Apr. 14, 2025
# This program determines whether a letter of the English
# alphabet entered by the user is a consonant, vowel,
# or semivowel. It also allows the user to find extra
# information about a particular letter by displaying
# phonetic symbols and examples if desired.

# Import the constants module to use constants.
import constants


# Define the main function.
def main():
    # Construct an infinite while loop for the letter input.
    while True:
        # Get the desired letter from the user.
        user_letter = input(
            f"{constants.DARK_GRAY}Enter a letter from a-z or A-Z:{constants.WHITE}\n"
        )

        # Checks if the lowercase form of the letter
        # entered is a letter of the English alphabet.
        if user_letter.lower() in constants.ENGLISH_LETTERS:
            # Break the infinite loop.
            break
        # Otherwise, they did not enter a valid letter.
        else:
            # Display to the user that they must enter
            # a valid letter of the English alphabet.
            print(
                f"""\n{constants.LIGHT_RED}{user_letter} is not a valid letter of the English alphabet.
Please enter a letter from a-z or A-Z.{constants.WHITE}\n"""
            )

    # Construct an infinite while loop for the display input.
    while True:
        # Get the desired display type from the user.
        user_display_type = input(
            f"""\n{constants.LIGHT_CYAN}Enter a display type for the letter.
Choices are "simple" (less detailed answer), and "complex" (more detailed answer):{constants.WHITE}\n"""
        )

        # Check if the lowercase form of simple
        # or complex was the entered display type.
        if (user_display_type.lower() == "simple") or (
            user_display_type.lower() == "complex"
        ):
            # Break the infinite loop.
            break
        # Otherwise, they did not enter a valid display type.
        else:
            # Display to the user that they must enter a valid choice.
            print(
                f"""\n{constants.LIGHT_RED}{user_display_type} is not a valid choice.
Please enter either simple or complex for the display type.{constants.WHITE}"""
            )

    # Construct an infinite while loop
    # for the phonetic symbol choice input.
    while True:
        # Get the user's choice of displaying a
        # phonetic symbol for their desired letter.
        show_phonetic_symbol_str = input(
            f"""\n{constants.LIGHT_YELLOW}Do you want a phonetic symbol to be displayed for the sound your letter makes?
Choices are "0" for no and "1" for yes:{constants.WHITE}\n"""
        )

        # Try to validate and proceed with the
        # user's choice for a phonetic symbol.
        try:
            # Attempt to convert the entered string into an integer.
            show_phonetic_symbol_int = int(show_phonetic_symbol_str)

            # Check if the user entered 0 for no or 1 for yes.
            if (show_phonetic_symbol_int == 0) or (show_phonetic_symbol_int == 1):
                # Construct a nested infinite while loop
                # for the phonetic example choice input.
                while True:
                    # Get the user's choice of displaying a
                    # phonetic word for their letter.
                    show_phonetic_example_str = input(
                        f"""\n{constants.LIGHT_BLUE}Do you want a phonetic word to be displayed as an example relating to your chosen letter?
Enter 0 for no or 1 for yes:{constants.WHITE}\n"""
                    )
                    # Try to validate and proceed with the
                    # user's choice for a phonetic example.
                    try:
                        # Attempt to convert the entered string into an integer.
                        show_phonetic_example_int = int(show_phonetic_example_str)

                        # Check if the user entered 0 for no
                        # or 1 for yes for the phonetic example.
                        if (show_phonetic_example_int == 0) or (
                            show_phonetic_example_int == 1
                        ):
                            # Break the inner infinite while loop.
                            break
                        # Otherwise, the user entered an integer
                        # out of range for the example choice.
                        else:
                            # Display to the user that they must enter 0 for no
                            # or 1 for yes for the phonetic example.
                            print(
                                f"""\n{constants.LIGHT_RED}{show_phonetic_example_int} is out of range for choices. 
Please enter either 0 for no or 1 for yes.{constants.WHITE}"""
                            )
                    # Runs if int() could not convert the user's string
                    # input into an integer for the example choice.
                    except ValueError:
                        # Display to the user that they need to enter
                        # a valid integer for the example choice.
                        print(
                            f"""\n{constants.LIGHT_RED}{show_phonetic_example_str} is not a valid integer.
Please enter a valid integer.{constants.WHITE}"""
                        )
                # Break the outer infinite while loop.
                break
            # Otherwise, the user entered an integer out of range
            # for the symbol choice.
            else:
                # Display to the user that they must enter 0 for no
                # or 1 for yes for the phonetic symbol.
                print(
                    f"""\n{constants.LIGHT_RED}{show_phonetic_symbol_int} is out of range for choices.
Please enter either 0 for no or 1 for yes.{constants.WHITE}"""
                )
        # Runs if int() could not convert the user's string
        # input into an integer for the symbol choice.
        except ValueError:
            # Display to the user that they need to enter
            # a valid integer for the symbol choice.
            print(
                f"""\n{constants.LIGHT_RED}{show_phonetic_symbol_str} is not a valid integer.
Please enter a valid integer.{constants.WHITE}"""
            )

    # Determine the place of the lowercase chosen letter in the
    # English alphabet by finding its index in the array of English
    # letters and adding it by 1.
    letter_place = constants.ENGLISH_LETTERS.index(user_letter.lower()) + 1

    # Check if the letter place ends in 1 and does not end in 11.
    if (letter_place % 10 == 1) and (letter_place % 100 != 11):
        # Set the letter place to "st."
        letter_place_suffix = "st"
    # Otherwise, check if the letter place ends in 2 and does not end in 12.
    elif (letter_place % 10 == 2) and (letter_place % 100 != 12):
        # Set the letter place to "nd."
        letter_place_suffix = "nd"
    # Otherwise, check if the letter place ends in 3 and does not end in 13.
    elif (letter_place % 10 == 3) and (letter_place % 100 != 13):
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
        case (
            "b"
            | "c"
            | "d"
            | "f"
            | "g"
            | "h"
            | "j"
            | "k"
            | "l"
            | "m"
            | "n"
            | "p"
            | "q"
            | "r"
            | "s"
            | "t"
            | "v"
            | "x"
            | "z"
        ) if (user_display_type.lower() == "simple"):
            # Display to the user that their
            # letter in uppercase is a consonant.
            print(f"\n{constants.LIGHT_PURPLE}The letter {user_letter.upper()} is a consonant.{constants.WHITE}")

        # The consonant case when the user display type in lowercase is complex.
        case (
            "b"
            | "c"
            | "d"
            | "f"
            | "g"
            | "h"
            | "j"
            | "k"
            | "l"
            | "m"
            | "n"
            | "p"
            | "q"
            | "r"
            | "s"
            | "t"
            | "v"
            | "x"
            | "z"
        ) if (user_display_type.lower() == "complex"):
            # Display to the user that their letter in uppercase
            # is a consonant with more information.
            print(
                f"""\n{constants.BROWN}The letter {user_letter.upper()}, the {letter_place}{letter_place_suffix} letter of the English alphabet, 
is a consonant. Consonants are speech sounds made with some or complete closure of the vocal tract.{constants.WHITE}"""
            )

        # The vowel case when the user display type in lowercase is simple.
        case "a" | "e" | "i" | "o" | "u" if user_display_type.lower() == "simple":
            # Display to the user that their
            # letter in uppercase is a vowel.
            print(f"\n{constants.LIGHT_PURPLE}The letter {user_letter.upper()} is a vowel.{constants.WHITE}")

        # The vowel case when the user display type in lowercase is complex.
        case "a" | "e" | "i" | "o" | "u" if user_display_type.lower() == "complex":
            # Display to the user that their letter in
            # uppercase is a vowel with more information.
            print(
                f"""\n{constants.BROWN}The letter {user_letter.upper()}, the {letter_place}{letter_place_suffix} letter of the English alphabet,
                is a vowel. Vowels are speech sounds made with little to no closure of the vocal tract.{constants.WHITE}"""
            )

        # The semivowel case when the user display type in lowercase is simple.
        case "w" | "y" if user_display_type.lower() == "simple":
            # Display to the user that their
            # letter in uppercase is a semivowel.
            print(f"\n{constants.LIGHT_PURPLE}The letter {user_letter.upper()} is a semivowel.{constants.WHITE}")

        # The semivowel case when the user display type in lowercase is complex.
        case "w" | "y" if user_display_type.lower() == "complex":
            # Display to the user that their letter in
            # uppercase is a semivowel with more information.
            print(
                f"""\n{constants.BROWN}The letter {user_letter.upper()}, the {letter_place}{letter_place_suffix} letter of the English alphabet, "
                "is a semivowel. Semivowels are special speech sounds that share some characteristics of a vowel and a consonant.{constants.WHITE}"""
            )

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
        print(
            f"""\n{constants.LIGHT_CYAN}The phonetic notation for the letter {user_letter.upper()} "
when said in isolation is {corresponding_phonetic_symbol}.{constants.WHITE}"""
        )

    # Check if the user wanted a phonetic example
    # word to be displayed based on the letter.
    if show_phonetic_example_int == 1:
        # Set the corresponding symbol to the corresponding index
        # of the example words array.
        corresponding_example_word = constants.EXAMPLE_WORDS[corresponding_index]

        # Display to the user a word that uses
        # the letter they chose in uppercase.
        print(
            f"""\n{constants.LIGHT_CYAN}One example of a word that uses the letter {user_letter.upper()} is {corresponding_example_word}.{constants.WHITE}"""
        )

    # Finally, thank the user for using this program.
    print(f"\n{constants.LIGHT_GREEN}Thanks for using this program!{constants.WHITE}")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()

"""
Random password generator
Python version 3.9.11
Authored: Azariah Pundari or aztec-dev (https://github.com/aztec-dev).
"""

# Import libraries
import random
from string import ascii_letters
from string import digits
from string import punctuation 

MIN_LENGTH = 8
MENU = "1. Add special characters\n2. Add numbers\n3. Add letters\n4. Exit"
character_sequence = []

def main():
    print(MENU)

    # Generate the password
    password_length = int(input("Enter the length of the password: "))
    while password_length < MIN_LENGTH:
        print(f"Password length should be at least {MIN_LENGTH} characters.")
        password_length = int(input("Enter the length of the password: "))

    # Get options
    option_number = int(input("Enter the number of options: "))
    while len(character_sequence) < 3:
        password = determine_password(option_number)
        option_number = int(input("Enter the number of options: "))
    print(len(password))
      
    for i in range(password_length):
        random_sequence = random.choice(password)
        print(random.choice(random_sequence), end="")

def determine_password(option_number):
    """Determines the password based on the number/option passed into the function."""
    if option_number == 1:
        character_sequence.append(punctuation)
    elif option_number == 2:
        character_sequence.append(digits)
    elif option_number == 3:
        character_sequence.append(ascii_letters)
        # TODO: work on exiting loop and error checking
    return character_sequence

if __name__ == "__main__":
    main()
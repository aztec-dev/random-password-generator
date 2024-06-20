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

def main():
    # Define the variables
    MIN_LENGTH = 8
    character_sequence = []

    # Generate the password
    password_length = int(input("Enter the length of the password: "))
    if password_length < MIN_LENGTH:
        print(f"Password length should be at least {MIN_LENGTH} characters.")
    else:
        character_sequence.append(ascii_letters)
        character_sequence.append(digits)
        character_sequence.append(punctuation)
        
    for i in range(password_length):
        random_sequence = random.choice(character_sequence)
        print(random.choice(random_sequence), end="")




if __name__ == "__main__":
    main()
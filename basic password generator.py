# password_cli.py
# Beginner: Random Password Generator with multiple outputs

import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    """Generate a random password based on selected character sets."""
    character_pool = ""
    
    if use_letters:
        character_pool += string.ascii_letters  # a-z + A-Z
    if use_digits:
        character_pool += string.digits         # 0-9
    if use_symbols:
        character_pool += string.punctuation    # !@#$%^&* etc.

    if not character_pool:
        raise ValueError("No character sets selected. Please enable at least one option.")

    return "".join(random.choice(character_pool) for _ in range(length))

def main():
    print("=== Random Password Generator ===")
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("⚠️ Password length must be greater than 0.")
            return

        count = int(input("How many passwords do you want to generate? "))
        if count <= 0:
            print("⚠️ Number of passwords must be greater than 0.")
            return

        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        print("\n✅ Generated Passwords:")
        for i in range(count):
            password = generate_password(length, use_letters, use_digits, use_symbols)
            print(f"{i+1}. {password}")

    except ValueError:
        print("⚠️ Invalid input. Please enter valid numbers for length and count.")

if __name__ == "__main__":
    main()

import random
import string

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + symbols

    # Ensure at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password to randomize character positions
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

def main():
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    password = generate_password(length)
    print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    main()
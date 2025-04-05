import secrets
import string

def get_password_length():
    while True:
        user_input = input("Enter the password length (default is 10, maximum 256):\n> ").strip()
        if user_input == "":
            return 10
        if user_input.isdigit():
            length = int(user_input)
            if 4 <= length <= 256:
                return length
            else:
                print("\n! The length must be from 4 to 256 characters (at least 4 — according to the number of required characters)!\n")
        else:
            print("\n! Enter a number or press Enter for the default value!\n")

def get_starting_letter():
    user_input = input("What letter should the password begin with? (Enter — random):\n> ").strip()
    if user_input == "":
        return secrets.choice(string.ascii_letters)
    elif len(user_input) == 1 and user_input in string.ascii_letters:
        return user_input
    else:
        print("\n! You need to enter one English letter. A random one is selected!\n")
        return secrets.choice(string.ascii_letters)

def generate_password(length, start_letter):
    if length < 4:
        raise ValueError("The password must be at least 4 characters long")

    required = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining_length = length - 1 - len(required)

    middle = [secrets.choice(all_chars) for _ in range(remaining_length)]
    all_chars_list = required + middle
    secrets.SystemRandom().shuffle(all_chars_list)

    return start_letter + ''.join(all_chars_list)

print('Secure Password Generator')
passwd_length = get_password_length()
passwd_start_letter = get_starting_letter()
password = generate_password(passwd_length, passwd_start_letter)
print(f"\nGenerated password:\n{password}")
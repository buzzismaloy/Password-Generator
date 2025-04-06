# Secure Password Generator

An interactive secure password generator written in Python. It uses cryptographically secure methods via the built-in `secrets` module.

The program works in an interactive mode: it prompts the user for input and generates a password that meets basic security requirements.

---

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/buzzismaloy/Password-Generator.git
    ```

2. Make sure you have Python 3 installed:
    ```bash
    python3 --version
    ```

3. Run the script:
    ```bash
    python3 password_generator.py
    ```

4. Follow the prompts:
    - Enter the desired password length (default is 10, maximum is 256)
    - Enter the starting letter (optional — leave empty for a random letter)

---

## Features

- Interactive CLI interface
- Secure generation using the `secrets` module
- Flexible password length configuration
- Optional custom starting letter
- Guaranteed inclusion of at least:
  - 1 lowercase letter (`a-z`)
  - 1 uppercase letter (`A-Z`)
  - 1 digit (`0-9`)
  - 1 special character (`!@#...`)

---

## Dependencies

No external dependencies are required — all libraries used are part of the Python standard library:

* `secrets`
* `string`

---

## Code Structure

The password always includes at least one character of each required type and starts with the specified (or randomly chosen) letter.

```python
get_password_length()      # Prompts the user for password length
get_starting_letter()      # Prompts the user for a starting letter
generate_password()        # Generates the password based on user input
```

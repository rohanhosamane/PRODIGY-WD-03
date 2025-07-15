import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\-=/\\|]", password) is None

    # Count the total number of errors
    errors = sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

    print("\nPassword Feedback:")
    if length_error:
        print("- Must be at least 8 characters long.")
    if digit_error:
        print("- Must include at least one digit.")
    if uppercase_error:
        print("- Must include at least one uppercase letter.")
    if lowercase_error:
        print("- Must include at least one lowercase letter.")
    if symbol_error:
        print("- Must include at least one special character.")

    # Strength level
    if errors == 0:
        return "Strong ✅"
    elif errors <= 2:
        return "Moderate ⚠️"
    else:
        return "Weak ❌"

# Input from user
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"\nPassword Strength: {strength}")

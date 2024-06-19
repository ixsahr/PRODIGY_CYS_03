import string


def check_password_strength(password):
    """
    Check the strength of a given password based on defined criteria.

    Args:
        password (str): The password to check.

    Returns:
        tuple: A tuple containing the strength score (int) and a list of suggestions (str).
    """
    # Define criteria for password strength
    length_criteria = 8
    uppercase_criteria = False
    lowercase_criteria = False
    number_criteria = False
    special_char_criteria = False

    # Initialize suggestions list
    suggestions = []

    # Check length
    length_criteria_passed = len(password) >= length_criteria
    if not length_criteria_passed:
        suggestions.append(f"Password should be at least {length_criteria} characters long.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        uppercase_criteria = True
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        lowercase_criteria = True
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    # Check for numbers
    if any(char.isdigit() for char in password):
        number_criteria = True
    else:
        suggestions.append("Add at least one number (0-9).")

    # Check for special characters
    if any(char in string.punctuation for char in password):
        special_char_criteria = True
    else:
        suggestions.append("Add at least one special character (!, @, #, etc.).")

    # Calculate overall strength
    strength = sum(
        [length_criteria_passed, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    return strength, suggestions


def main():
    # Get password input from user
    password = input("Enter your password: ")

    # Check password strength
    strength, suggestions = check_password_strength(password)

    # Provide feedback based on strength
    strength_messages = {
        5: "Password is very strong!",
        4: "Password is strong.",
        3: "Password is moderate.",
        2: "Password is weak.",
        1: "Password is very weak.",
        0: "Password does not meet minimum criteria."
    }

    print(strength_messages[strength])

    if suggestions:
        print("Suggestions to improve your password:")
        for suggestion in suggestions:
            print(f"- {suggestion}")


if __name__ == "__main__":
    main()

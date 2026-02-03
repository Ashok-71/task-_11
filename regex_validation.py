import re

# Email validation function
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.fullmatch(pattern, email) is not None


# Indian mobile number validation function
def validate_mobile(mobile):
    pattern = r'^[6-9]\d{9}$'
    return re.fullmatch(pattern, mobile) is not None


# Password validation function
def validate_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    return re.fullmatch(pattern, password) is not None


def main():
    print("=== REGEX DATA VALIDATION ===")

    email = input("Enter email address: ").strip()
    if validate_email(email):
        print("✅ Email is valid")
    else:
        print("❌ Invalid email format")

    mobile = input("Enter Indian mobile number: ").strip()
    if validate_mobile(mobile):
        print("✅ Mobile number is valid")
    else:
        print("❌ Invalid mobile number")

    password = input("Enter password: ").strip()
    if validate_password(password):
        print("✅ Password is strong")
    else:
        print("❌ Password must be at least 8 characters and include letters, numbers, and special characters")


if __name__ == "__main__":
    main()

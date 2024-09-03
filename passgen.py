def generate_password(length):
    if length < 6:
        print("Password length should be at least 6 characters.")
        return

    # Define the characters to be used in the password
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punctuation = '!@#$%^&*()'

    # Combine all the characters
    all_characters = lowercase + uppercase + digits + punctuation

    # Generate a random password
    password = ''
    for _ in range(length):
        index = (len(password) * 7) % len(all_characters)  # Simple pseudo-random index generation
        password += all_characters[index]

    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired password length (at least 6): "))
    password = generate_password(length)
    if password:
        print(f"Generated password: {password}")

if _name_ == "_main_":
    main()
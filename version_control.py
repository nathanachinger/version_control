# Nathan Achinger.

def encode():
    encoded_password = []
    password = input("Please enter your password to encode: ")
    for digit in password:
        encoded_password.append(int(digit)+3)
    print("Your password has been encoded and stored!")

def decode():
    pass


if __name__ == '__main__':
    while True:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        user_input = input("\nPlease enter an option: ")
        if user_input == '1':
            encode()
        elif user_input == '2':
            decode()
        elif user_input == '3':
            break


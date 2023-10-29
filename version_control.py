# Nathan Achinger

def encode():
    password = input("Please enter your password to encode: ")
    encoded_password = [str((int(digit)-7)) if int(digit) > 6 else str((int(digit)+3)) for digit in password]
    return ''.join(encoded_password)


def decode():
    decoded_password = ''
    print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")


if __name__ == '__main__':
    while True:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        user_input = input("\nPlease enter an option: ")
        if user_input == '1':
            encoded_password = encode()
        elif user_input == '2':
            decode()
        elif user_input == '3':
            break


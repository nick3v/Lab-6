# Code created by Nicolas Espinoza
def main():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')


def encode():
    user_pass = list(input('Please enter your password to encode: '))  # List to iterate each number
    for i in range(len(user_pass)):
        user_pass[i] = str((int(user_pass[i]) + 3) % 10)  # Changes each element to an integer, adds 3, then back to string
    print('Your password has been encoded and stored!')
    return ''.join(user_pass)  # Returns a string of the encoded password

def decode(password):
    # Created by Shiner Supre
    decoded_password = ""
    for digit in password:
        # Converts the character to an integer, subtracts 3 from each, and appends to an empty string
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


if __name__ == '__main__':
    user_choice = '0'
    while user_choice != '3':
        main()
        user_choice = input('Please enter an option: ')
        if user_choice not in ['1', '2', '3']:
            continue
        elif user_choice == '1':
            encoded_pass = encode()  # Assigns the encoded password string for further use
        elif user_choice == '2':
            decoded_pass = decode(encoded_pass) # Decodes the stored encoded password
            print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}.')
    exit()

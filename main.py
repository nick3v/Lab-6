# Code created by Nicolas Espinoza
def main():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')


def encode():
    user_pass = list(input('Please enter your password to encode: '))  # List to iterate each number
    for i in range(len(user_pass)):
        user_pass[i] = str(int(user_pass[i]) + 3)  # Changes each element to an integer, adds 3, then back to string
    print('Your password has been encoded and stored!')
    return ''.join(user_pass)  # Returns a string of the encoded password


if __name__ == '__main__':
    user_choice = '0'
    while user_choice != '3':
        main()
        user_choice = input('Please enter an option: ')
        if user_choice not in ['1', '2', '3']:
            continue
        elif user_choice == '1':
            encoded_pass = encode()  # Assigns the encoded password string for further use
    exit()

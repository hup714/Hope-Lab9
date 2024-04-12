str_pw = ''


def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")


def main():
    option = int(input("Please enter an option: "))
    if option == 1:
        encode()
    elif option == 2:
        pass
    elif option == 3:
        exit()


def encode():
    encoded_pw = []
    global str_pw
    password = str(input("Please enter your password to encode: "))
    print("Your password has been encoded and stored!\n")
    for i in password:
        encoded_pw.append(int(i) + 3)
        if int(i) >= 7:
            if int(i) == 7:
                encoded_pw.append(0)
            elif int(i) == 8:
                encoded_pw.append(1)
            elif int(i) == 9:
                encoded_pw.append(2)
    for j in encoded_pw:
        str_pw += str(j)
    return str_pw


if __name__ == '__main__':
    while True:
        menu()
        main()

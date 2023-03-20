def main():
    password = get_password()
    make_asterisks(password)


def make_asterisks(password):
    print(f"Your password is: {'*' * len(password)}")


def get_password():
    password = input("Password: ")
    while len(password) < 6:
        print("Password too short")
        password = input("Password: ")
    return password


main()


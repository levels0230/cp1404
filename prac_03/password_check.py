
def main():
    password = get_password()
    print_to_star(password)


def get_password():
    password = input("Enter  password: ")
    return password


def print_to_star(password):
    print("*" * len(password))


main()

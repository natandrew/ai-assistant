def get_operation():
    print("\n" + "Choose operation:", "+", "-", "*", "/", sep="\n")

    return input()


def get_numbers():
    print("\n" + "Enter 2 numbers...")

    return int(input()), int(input())

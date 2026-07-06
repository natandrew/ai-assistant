import random


def get_degrees():
    print(
        "\n" + "How does the weather feel today?",
        "1. Cold",
        "2.Chilly",
        "3. Warm",
        "4. Hot",
        sep="\n",
    )

    weather = int(input())

    print("\n" + "Also tell me the city that you're in:")

    city = input()
    message = "\n" + f"Indeed, in {city} there are"

    match weather:
        case 1:
            print(message, f"{random.randint(-30, 0)} degrees Celsius", end="\n\n")
        case 2:
            print(message, f"{random.randint(1, 14)} degrees Celsius", end="\n\n")
        case 3:
            print(message, f"{random.randint(15, 20)} degrees Celsius", end="\n\n")
        case 4:
            print(message, f"{random.randint(21, 40)} degrees Celsius", end="\n\n")

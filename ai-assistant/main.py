import calculator
import joke
import passwordGenerator
import weather
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / "History.txt"


def main():
    n = 1
    print("> Hello!", end="\n\n")
    print("What's your name?")

    name = input()

    print("\n" + f"Hello {name}!", end="\n\n")

    while n:
        print(
            "1. Calculator",
            "2. Weather",
            "3. Tell a joke",
            "4. Generate password",
            "5. Quit",
            sep="\n",
            end="\n\n",
        )
        print("Choose:")

        choice = input()

        with open(file_path, "a") as file:
            if choice == "1":
                file.write("Used calculator\n")
            elif choice == "2":
                file.write("Asked for weather\n")
            elif choice == "3":
                file.write("Asked for a joke\n")
            elif choice == "4":
                file.write("Generated a password\n")
            elif choice == "5":
                file.write("Quit the program\n")

        match choice:
            case "1":
                op = calculator.get_operation()
                a, b = calculator.get_numbers()

                if op == "+":
                    print("Result:", a + b, end="\n\n")
                elif op == "-":
                    print("Result:", a - b, end="\n\n")
                elif op == "*":
                    print("Result:", a * b, end="\n\n")
                elif op == "/":
                    print("Result:", a / b, end="\n\n")

                continue
            case "2":
                weather.get_degrees()

                continue
            case "3":
                joke.get_joke()

                continue
            case "4":
                passwordGenerator.pw()

                continue

            case "5":
                break


if __name__ == "__main__":
    main()

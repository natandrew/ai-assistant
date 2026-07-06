# AI Assistant (Python CLI)

A simple command-line AI-inspired assistant built with Python. The assistant provides several useful utilities through an interactive menu, helping me practice Python fundamentals such as functions, modules, file handling, user input, and randomization.

## Features

* 🧮 **Calculator**

  * Supports addition, subtraction, multiplication, and division.

* 🌤️ **Weather Simulator**

  * Asks how the weather feels and the user's city.
  * Generates a random temperature that matches the selected weather condition.

* 😂 **Random Joke Generator**

  * Displays a random joke from a predefined collection.

* 🔐 **Password Generator**

  * Generates a random 8-character password using letters, numbers, and symbols.

* 📝 **History Logging**

  * Records each action the user performs in `History.txt`.

## Project Structure

```text
ai-assistant/
│
├── main.py                 # Main application
├── calculator.py           # Calculator functionality
├── weather.py              # Weather simulator
├── joke.py                 # Joke generator
├── passwordGenerator.py    # Password generator
├── History.txt             # Stores user activity
```

## Requirements

* Python 3.10 or newer

No external libraries are required. The project only uses Python's standard library.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/natandrew/ai-assistant.git
```

2. Navigate into the project folder:

```bash
cd ai-assistant
```

3. Run the application:

```bash
python main.py
```

## Example

```text
> Hello!

What's your name?
Andrew

Hello Andrew!

1. Calculator
2. Weather
3. Tell a joke
4. Generate password
5. Quit
```

Choose an option by entering its corresponding number.

## What I Learned

Building this project helped me practice several core Python concepts:

* Organizing code into multiple modules.
* Importing and using custom Python files.
* Writing reusable functions.
* Working with user input and output.
* Using conditional statements and `match` expressions.
* Reading from and writing to text files.
* Generating random values using the `random` module.
* Using built-in modules such as `string` and `pathlib`.
* Structuring a simple command-line application.

Although this is a beginner project, it gave me experience splitting functionality into separate files and creating a more maintainable program.

# Python Workshop: Create Phase Problem Set

These exercises are designed to help you practice the concepts of modules, virtual environments, and package management. Try to solve them independently after the workshop.

## Instructions:

1.  For each problem, create a **new project directory**.
2.  Inside each new project directory, create and activate a **new virtual environment**.
3.  Write your Python scripts (`.py` files) within these project directories.
4.  If a problem requires external packages, install them into the project's virtual environment using `pip`.
5.  For each project, generate a `requirements.txt` file.

---

### Problem 1: Simple Daily Greeter

**Objective:** Create a script that greets the user with a random positive message and shows the current date.

**Requirements:**
1.  Create a new project directory (e.g., `daily_greeter`).
2.  Set up a virtual environment inside it.
3.  Write a Python script (`greeter.py`) that does the following:
    *   Uses the `datetime` module to get and print the current date (e.g., "Today is: YYYY-MM-DD").
    *   Uses the `random` module to select and print a random positive greeting from a list of at least 5 predefined greetings.
      *   Example greetings: "Have a wonderful day!", "You're doing great!", "Keep up the amazing work!", "Shine bright today!", "Good things are coming your way!"
4.  Generate a `requirements.txt` file for this project (even if it only contains built-in module usage, it's good practice to generate it, though it might be empty or show system packages if not careful with venv for this specific case; the main point is the script logic).

**Example Output:**
```
Today is: 2023-10-27
Your positive message for the day: Have a wonderful day!
```

---

### Problem 2: Fun with ASCII Art

**Objective:** Use an external package to display some text as ASCII art.

**Requirements:**
1.  Create a new project directory (e.g., `ascii_fun`).
2.  Set up and activate a virtual environment.
3.  Find a simple package on PyPI (https://pypi.org/) that can convert text to ASCII art. A good candidate is the `art` package (`pip install art`).
4.  Write a Python script (`ascii_converter.py`) that:
    *   Imports the chosen package.
    *   Asks the user to input a short text (e.g., their name or "Python").
    *   Uses the package to convert this text into ASCII art and print it to the console.
    *   (Optional bonus) Explore the package's documentation. Can you change the font or style of the ASCII art?
5.  Generate a `requirements.txt` file for this project. It should list the ASCII art package you installed.

**Example Interaction (using the `art` package):**
```
Enter text to make into ASCII art: Hello
 _   _      _ _       
| | | | ___| | | ___  
| |_| |/ _ \ | |/ _ \ 
|  _  |  __/ | | (_) |
|_| |_|\___|_|_|\___/ 
                      
```

---

### Problem 3 (Challenge): Mini Number Guessing Game

**Objective:** Create a simple number guessing game using modules, and manage its (hypothetical) dependencies.

**Requirements:**
1.  Create a new project directory (e.g., `guessing_game`).
2.  Set up and activate a virtual environment.
3.  Write a Python script (`game.py`) that:
    *   Uses the `random` module to pick a secret number between 1 and 20.
    *   Uses the `datetime` module to record the start time of the game.
    *   Allows the user up to 5 guesses.
    *   For each guess:
        *   Tell the user if their guess is too high, too low, or correct.
        *   If correct, congratulate them, print how many guesses it took, and how long they played (difference between start time and end time). Then, exit the game.
    *   If the user runs out of guesses, tell them the secret number and how long they played.
    *   **Dependency aspect:** Imagine this game *also* used a (fictional or real simple) package, say `colorama` (for colored terminal text) to make the output prettier. Even if you don't fully implement colored text, install `colorama` (`pip install colorama`) into your venv for this project.
4.  Generate a `requirements.txt` file. It should list `colorama` (or any other package you chose to "simulate" a dependency with).

**Example Interaction:**
```
Welcome to the Number Guessing Game!
I've picked a number between 1 and 20. You have 5 guesses.
Game started at: 2023-10-27 14:30:00.123456
Guess 1: 10
Too low!
Guess 2: 15
Too high!
Guess 3: 13
Congratulations! You guessed it in 3 tries.
You played for 0:00:15.678910 seconds.
```
(If they fail):
```
...
Guess 5: 19
Too high!
Sorry, you ran out of guesses. The number was 17.
You played for 0:00:25.123456 seconds.
```

Good luck!
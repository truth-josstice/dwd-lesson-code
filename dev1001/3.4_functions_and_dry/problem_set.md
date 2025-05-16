**CREATE Phase: Homework Problem Set**

**Problem 1: Simple Temperature Converter**
*   **Task:** Write a Python script that includes two functions:
    1.  `celsius_to_fahrenheit(celsius)`: Takes a temperature in Celsius (float) and returns the equivalent in Fahrenheit (float). Formula: `F = C * 9/5 + 32`.
    2.  `fahrenheit_to_celsius(fahrenheit)`: Takes a temperature in Fahrenheit (float) and returns the equivalent in Celsius (float). Formula: `C = (F - 32) * 5/9`.
*   **Main Script:**
    *   Prompt the user to enter a temperature and its unit (C or F).
    *   Call the appropriate function to convert it.
    *   Print the original and converted temperatures neatly.
    *   Example: "25.0°C is 77.0°F" or "68.0°F is 20.0°C".

**Problem 2: Basic Library Book Checkout Message**
*   **Task:** Create a function `generate_checkout_message(book_title, member_name, due_days=14)`.
    *   `book_title` (string): The title of the book.
    *   `member_name` (string): The name of the library member.
    *   `due_days` (int, optional): Number of days until the book is due. Defaults to 14 days.
*   The function should return a formatted string like:
    `"Dear [member_name], thank you for checking out '[book_title]'. It is due back in [due_days] days. Happy reading!"`
*   **Main Script:**
    *   Call this function at least three times with different inputs to demonstrate:
        *   Using only positional arguments (and the default `due_days`).
        *   Using keyword arguments for all parameters.
        *   Using a mix and overriding the `due_days` (e.g., for a short-loan item, `due_days=3`).
    *   Print the returned message for each call.

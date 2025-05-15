## "Create" Phase Exercises (Homework)

**General Instructions for Students:** For each problem, aim to use the concepts of dictionaries and loops we discussed. Think about how these structures can help you organize and process the data efficiently. Avoid using user-defined functions (`def`) for these exercises.

One reason to forbid user-defined functions is that we haven't covered them yet! But another good reason is to simulate real-world development where we are often under several constraints and can't always build a solution exactly how we want to.

**NOTE: Advanced Challenges are OPTIONAL!**

---

**Topic 1: Dictionaries - "Create" Exercises**

**Create 1.1: Student Report Card Generator**

*   **Problem:** You need to store and display student grades for several subjects.
*   **Task:**
    1.  Create a dictionary where keys are student names (strings) and values are *another dictionary*. This inner dictionary should store subject names (strings) as keys and their corresponding grades (integers, 0-100) as values.
    2.  Populate this main dictionary with data for at least 3 students, each with at least 3 subjects (e.g., "Math", "Science", "History").
    3.  Write code that iterates through the main dictionary. For each student, print their name and then list each subject and their grade.
    4.  Calculate and print the average grade for one specific student of your choice.
*   **Example Structure:**
    ```python
    student_data = {
        "Alice Wonderland": {"Math": 90, "Science": 85, "Literature": 92},
        "Bob The Builder": {"Math": 70, "Science": 75, "Workshop": 95},
        # ... more students
    }
    ```
*   **Advanced Challenge 1.1:**
    *   After printing each student's report, also identify and print their highest-scoring subject and their lowest-scoring subject. If there are ties, any of the tied subjects is fine.
    *   *(Hint: You'll need to iterate through the inner dictionary's items and keep track of the max/min score found so far.)*

**Create 1.2: Simple Word Frequency Counter**

*   **Problem:** Given a paragraph of text (as a multi-line string), count how many times each word appears.
*   **Task:**
    1.  Store the following sample text in a variable:
        ```
        text = """
        This is a sample text. This text is for a sample programming exercise.
        The exercise is to count words in this text.
        Ignore case and punctuation for simplicity.
        """
        ```
    2.  Pre-process the text:
        *   Convert it all to lowercase.
        *   Remove common punctuation (e.g., periods `.`, commas `,`). You can use string `.replace()` method multiple times.
        *   Split the text into a list of words using `.split()`.
    3.  Create an empty dictionary.
    4.  Iterate through your list of words. For each word:
        *   If the word is already a key in your dictionary, increment its value (count).
        *   If the word is not yet a key, add it to the dictionary with a value of 1.
    5.  After processing all words, print the dictionary of word frequencies.
    6.  Then, print each word and its count in a more readable format (e.g., "word: count").
*   **Advanced Challenge 1.2:**
    *   Modify your output to print the words sorted alphabetically.
    *   Then, modify it again to print the words sorted by their frequency (most frequent first). If frequencies are tied, alphabetical order for those words is fine.
    *   *(Hint: For sorting dictionary items, you might need to convert `dictionary.items()` to a list and then use `list.sort()` or the `sorted()` built-in function, possibly with a `lambda` key in the future, but for now, you might have to create lists of tuples and sort those.)*

---

**Topic 2: Loops - "Create" Exercises**

**Create 2.1: Interactive Shopping List Manager**

*   **Problem:** Create a simple command-line shopping list manager.
*   **Task:**
    1.  Initialize an empty list called `shopping_list`.
    2.  Use a `while True` loop to continuously prompt the user for actions until they choose to exit.
    3.  Inside the loop, display a menu of options:
        *   "1. Add item"
        *   "2. View list"
        *   "3. Mark item as purchased (remove)"
        *   "4. Exit"
    4.  Get the user's choice.
    5.  Based on the choice:
        *   **Add:** Prompt for the item name and add it to `shopping_list`.
        *   **View:** If the list is empty, print "Your shopping list is empty." Otherwise, use `enumerate` to display the items with a number (e.g., "1. Apples", "2. Bananas").
        *   **Mark as purchased:**
            *   If the list is empty, print "List is empty, nothing to remove."
            *   Otherwise, display the list with numbers (like in "View"). Prompt the user for the *number* of the item to remove.
            *   Validate the input: ensure it's a valid number corresponding to an item in the list.
            *   If valid, remove the item using `del shopping_list[index]` or `shopping_list.pop(index)`. Inform the user.
        *   **Exit:** Print "Goodbye!" and `break` out of the `while` loop.
        *   **Invalid choice:** Print "Invalid option, please try again."
*   **Advanced Challenge 2.1:**
    *   When adding an item, prevent duplicate entries. If the user tries to add an item already on the list, inform them.
    *   For "Mark as purchased", allow the user to type the *name* of the item to remove instead of its number. Handle cases where the item name isn't found.
    *   *(Hint: You'll use `in` operator and list methods like `.index()` or iterate to find items by name.)*

**Create 2.2: Batch User Data Processing**

*   **Problem:** You have a list of user data (as a list of dictionaries) and need to perform some batch processing.
*   **Task:**
    1.  Start with the following list of dictionaries:
        ```python
        users = [
            {"id": "user1", "name": "Alice", "email_verified": True, "logins_last_month": 15},
            {"id": "user2", "name": "Bob", "email_verified": False, "logins_last_month": 3},
            {"id": "user3", "name": "Charlie", "email_verified": True, "logins_last_month": 22},
            {"id": "user4", "name": "David", "email_verified": True, "logins_last_month": 8},
            {"id": "user5", "name": "Eve", "email_verified": False, "logins_last_month": 30},
        ]
        ```
    2.  **Identify Inactive Users:**
        *   Create an empty list called `inactive_user_ids`.
        *   Iterate through the `users` list. If a user has `logins_last_month` less than 5, add their `id` to `inactive_user_ids`.
        *   Print the `inactive_user_ids` list.
    3.  **Send Verification Reminders:**
        *   Create an empty list called `needs_verification_reminder`.
        *   Iterate through the `users` list. If a user has `email_verified` set to `False`, add their `name` to `needs_verification_reminder`.
        *   Print a message for each user in `needs_verification_reminder`, e.g., "Reminder sent to Bob to verify email."
    4.  **Calculate Total Logins:**
        *   Initialize a variable `total_logins` to 0.
        *   Iterate through the `users` list and sum up all `logins_last_month`.
        *   Print the `total_logins`.
*   **Advanced Challenge 2.2:**
    *   Identify the "Most Active User" (user with the highest `logins_last_month`). Print their name and login count. If there's a tie, any of the top users is fine.
    *   Create a new dictionary `engagement_segments` where keys are "low", "medium", "high" and values are lists of user IDs belonging to that segment (e.g., low: 0-9 logins, medium: 10-19, high: 20+).
    *   *(Hint: For most active, you'll need to iterate and keep track of the maximum value seen and the associated user. For segments, initialize the dictionary with empty lists and append user IDs as you iterate and check conditions.)*

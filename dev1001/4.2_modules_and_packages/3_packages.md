# Packages

## Modify

Your tasks:

1.  Modify `api_client.py` to fetch data for a *different* 'product ID' (e.g., 2 or 3 from JSONPlaceholder todos).
2.  Instead of just printing the title, extract and print both the `userId` and `completed` status from the fetched JSON data.
3.  (Optional) If the `requests` call fails (e.g., network issue, or try an invalid URL), ensure your program handles it gracefully (the `try-except` block already helps, but you can refine the error message).

---

## Create

Your tasks:

1.  Our project now depends on `requests`. To let other developers (or our future selves) easily set up the same environment, we need a `requirements.txt` file.
    *   In your terminal (with the e-commerce project's venv active), generate this file. What command would you use? (`pip freeze > requirements.txt`)
2.  Open `requirements.txt`. What do you see? It should list `requests` and its dependencies with their versions.
3.  (Simulate new setup - conceptual or actual if time allows): Imagine a colleague pulls your project. They would:
    *   Create a new venv.
    *   Activate it.
    *   Run `pip install -r requirements.txt`.
    This installs all necessary packages.
4.  **Challenge:** Suppose you also want to use a package to add color to your terminal output for better visual feedback (e.g., the `colorama` package or `rich` for more advanced features).
    *   Find one such package on PyPI (pypi.org).
    *   Install it using `pip`.
    *   Briefly use it in `api_client.py` (e.g., print the fetched title in a specific color - `colorama` is simpler for this).
    *   *Crucially:* Update your `requirements.txt` to include this new package.

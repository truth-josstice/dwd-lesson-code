'''
Problem 2: Simple CSV Data Writer (CSV Files)

Objective: Practice writing data to a CSV file.

Description:
You have a list of simple data representing contacts (name and email). Write a Python script that:

1. Creates a CSV file named contacts.csv.
2. Writes a header row: Name,Email.
3. Writes the contact data to the contacts.csv file, with each contact on a new row.
'''

import csv

CONTACTS_CSV_FILE = "contacts.csv"

def write_contacts_to_csv(contact_list):
    """
    Writes the contact_list data to CONTACTS_CSV_FILE.
    The first row should be a header: ["Name", "Email"].
    Each item in contact_list is a sublist like ["Alice", "alice@example.com"].
    """
    header = ["Name", "Email"]
    
    # TODO 1: Open CONTACTS_CSV_FILE in 'write' mode ('w').
    # Remember to include newline='' for CSV files.
    # Use a 'with' statement.
    # Inside the 'with' block:
    #     TODO 2: Create a csv.writer object.
    #     TODO 3: Write the header row using the writer.
    #     TODO 4: Write all the data rows from contact_list using the writer (e.g., writerows).

    print(f"Contact data written to {CONTACTS_CSV_FILE}")


# --- Test your function ---
if __name__ == "__main__":
    my_contacts = [
        ["Alice Wonderland", "alice@wonder.land"],
        ["Bob The Builder", "bob@builder.com"],
        ["Charlie Brown", "charlie@peanuts.com"]
    ]
    
    write_contacts_to_csv(my_contacts)

    # After running, check contacts.csv. It should look like:
    # Name,Email
    # Alice Wonderland,alice@wonder.land
    # Bob The Builder,bob@builder.com
    # Charlie Brown,charlie@peanuts.com

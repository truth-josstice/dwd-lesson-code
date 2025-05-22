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
    with open(CONTACTS_CSV_FILE, 'w', newline='') as f:
        # TODO 2: Create a csv.writer object.
        csv_writer = csv.writer(f)
        
        # TODO 3: Write the header row using the writer.
        csv_writer.writerow(header)
        
        # TODO 4: Write all the data rows from contact_list using the writer.
        csv_writer.writerows(contact_list)

    print(f"Contact data written to {CONTACTS_CSV_FILE}")

# --- Test your function ---
if __name__ == "__main__":
    my_contacts = [
        ["Alice Wonderland", "alice@wonder.land"],
        ["Bob The Builder", "bob@builder.com"],
        ["Charlie Brown", "charlie@peanuts.com"]
    ]
    
    write_contacts_to_csv(my_contacts)

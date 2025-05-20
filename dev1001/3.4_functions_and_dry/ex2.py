def generate_checkout_message (book_title, member_name, due_days=14):
    print(f"Dear {member_name}, thank you for checking out '{book_title}'. It is due back in {due_days} days. Happy reading!")
    return

generate_checkout_message("Moby Dick", "Jethro Tull")
generate_checkout_message(book_title="Coding for Dummies", member_name="Silly Dumberson", due_days=14)
generate_checkout_message("5 Ways to Subvert Mind Control", member_name="Jessica Jones", due_days=3)
import hashlib
import re

def get_name(prompt):
    while True:
        name = input(prompt)
        if len(name) <= 20:
            return name
        print("Error: Name must be 20 characters or less")

def get_email(prompt):
    email_check = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    while True:
        email = input(prompt)
        if re.fullmatch(email_check, email):
            return email
        print("Error: Not a valid email")
        
def get_password():
    while True:
        password = input("Password: ")
        retyped_password = input("Retype Password: ")
        if password == retyped_password:
            return password
        print("Error: Passwords did not match")

def get_float(prompt, type):
    weight_check = r"^\d{1,3}(\.\d{1,2})?$"
    while True:
        weight = input(prompt)
        if re.fullmatch(weight_check, weight):
            return weight
        print("Error: Not a valid", type)

def get_date(prompt):
    date_check = r"^\d{4}\-\d{2}\-\d{2}$"
    while True:
        date = input(prompt)
        if re.fullmatch(date_check, date):
            return date
        print("Error: Not a valid date format (yyyy-mm-dd)")

def create_account(cursor):
    # Get user information for account - should check if input is valid
    first_name = get_name("First Name: ")
    last_name = get_name("Last Name: ")
    email = get_email("Email: ")
    password = get_password()
    height = float(get_float("Height (Inches): ", "height"))
    weight = float(get_float("Weight (lbs): ", "weight"))
    goal_weight = float(get_float("Goal Weight: ", "weight"))
    goal_deadline = get_date("Deadline to reach goal weight (yyyy-mm-dd): ")

    # Hash the password
    h = hashlib.new("SHA256")
    h.update(password.encode())
    password_hash = h.hexdigest()

    # Attempt to enter into database
    cursor.execute("INSERT INTO users (first_name, last_name, email, password, role) VALUES (%s, %s, %s, %s, %s);", (first_name, last_name, email, password_hash, 'member'))
    cursor.execute("SELECT id FROM users WHERE email = %s;", (email,))
    member_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO members (member_id, goal_weight, goal_deadline, height, weight) VALUES (%s, %s, %s, %s, %s)", (member_id, goal_weight, goal_deadline, height, weight))
    
    print("\n--- Successfully Created Account! ---\n")

def login(cursor):
    email = input("Email: ")
    password = input("Password: ")

    # Get the hash value of the password to check against the database
    h = hashlib.new("SHA256")
    h.update(password.encode())
    password_hash = h.hexdigest()

    cursor.execute("SELECT id, role FROM users WHERE email = %s AND password = %s;", (email, password_hash))
    user = cursor.fetchone()

    if user is None:
        print("\n--- No user found or incorrect password ---\n")
    else:
        print("\n--- Logged in! ---\n")
        user_id, user_role = user
        return True, user_id, user_role  # Logged in
    return False, None, None  # Not logged in

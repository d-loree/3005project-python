import hashlib

def create_account(cursor):
    # Get user information for account - should check if input is valid
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password = "0"
    retyped_password = "1"
    while password != retyped_password:
        password = input("Password: ")
        retyped_password = input("Retype Password: ")
        if password != retyped_password:
            print("\nPasswords did not match")
    height = round(float(input("Height (Ft): ")), 2)
    weight = round(float(input("Weight (lbs): ")), 2)
    goal_weight = round(float(input("Goal Weight: ")), 2)
    goal_deadline = input("Deadline to reach goal weight (yyyy-mm-dd): ")

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

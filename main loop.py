import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
dbname = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Example: Execute a simple query
cursor.execute("SELECT version();")
version = cursor.fetchone()
print("PostgreSQL version:", version)

# Remember to close the cursor and connection when done
cursor.close()
conn.close()





while True:

    logged_in = False

    if logged_in == False:
        input("enter 1 to create and account and 2 to login, enter 3 to break")
        # verify credentials and login

    else:
        #if account type is user, display user functions, same for trainer, admin
        account_type = ""

        if account_type == "member":
            while True:
                input = input("enter 1 for schedule management, 2 for profile management, 3 for dashboard display, 4 to logout")
                if input == 1:
                    input = input("enter 1 for schedule personal training session, 2 for scheduling group fitenss class, 3 to exit")

                elif input == 2:
                    input = input("enter 1 for update fitness goals, enter 2 for editing health metric, enter 3 for editing personal info, 4 to exit")

                elif input == 3:
                    print()
                    #displaydashboard()


        elif account_type == "trainer":
            while True:
                input = input("enter 1 for schedule management, 2 for profile management, enter 3 for member profile viewing, 4 to logout")
                if input == 1:
                    input = input("enter 1 for setting avilibility, 2 to exit")

                elif input == 2:
                    input = input("TBD")

                elif input == 3:
                    print()
                    #displaydashboard()


        elif account_type == "admin":
            while True:
                input = input("enter 1 for room booking management, 2 for equipment maintenance monitoring, enter 3 for class schedule updating "
                      "4 for billing and payment processing, 5 to logout")
                if input == 1:
                    input = input("enter 1 for setting avilibility, 2 to exit")

                elif input == 2:
                    input = input("TBD")

                elif input == 3:
                    print()
                    #displaydashboard()


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
        input("1: Create New Account\n"
              "2: Login\n"
              "3: Quit")
        # verify credentials and login

    else:
        #if account type is user, display user functions, same for trainer, admin
        account_type = ""

        if account_type == "member":
            while True:
                user_input = input("1: Schedule Management\n"
                                   "2: Profile Management\n"
                                   "3: Dashboard Display\n"
                                   "4: Logout\n>>> ")
                if user_input == '1':
                    user_input = input("1: Schedule Personal Training Session\n"
                                       "2: Scheduling Group Fitenss Class\n"
                                       "3: Exit"
                                       "\n>>> ")

                elif user_input == '2':
                    user_input = input("1: Update Fitness Goals\n"
                                       "2: Editing Health Metrics\n"
                                       "3: Editing Personal Information\n"
                                       "4: Exit"
                                       "\n>>> ")

                elif user_input == '3':
                    print()
                    #displaydashboard()


        elif account_type == "trainer":
            while True:
                user_input = input("1: Schedule management\n"
                                   "2: Profile management\n"
                                   "3: Member Profile Viewing\n"
                                   "4: Logout"
                                       "\n>>> ")
                if user_input == '1':
                    user_input = input("1: Setting Availibility\n"
                                       "2: Exit"
                                       "\n>>> ")

                elif user_input == '2':
                    user_input = input("TBD")

                elif user_input == '3':
                    print()
                    #displaydashboard()


        elif account_type == "admin":
            while True:
                user_input = input( "1: Room Booking Management\n"
                                    "2: Equipment Maintenance Monitoring\n"
                                    "3: Class Schedule Updating\n"
                                    "4: Billing and Payment Processing\n"
                                    "5: Logout"
                                       "\n>>> ")
                if user_input == '1':
                    user_input = input("1: Setting Availibility\n"
                                       "2: Exit"
                                       "\n>>> ")

                elif user_input == '2':
                    user_input = input("TBD")

                elif user_input == '3':
                    print()
                    #displaydashboard()


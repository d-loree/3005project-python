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
    account_type = ""

    if logged_in == False:
        user_input = input( "1: Create New Account\n"
                            "2: Login\n"
                            "3: Quit")
        # Create New Account --------
        if user_input == '1':
            print()
        
        # Login --------
        elif user_input == '2':
            print()

        # Quit --------
        elif user_input == '3':
            print()

    else:
        #if account type is user, display user functions, same for trainer, admin

        if account_type == "member":
            while True:
                # Member Dashboard --------
                user_input = input("1: Schedule Management\n"
                                   "2: Profile Management\n"
                                   "3: Dashboard Display\n"
                                   "4: Logout\n>>> ")
                
                # Schedule Management --------
                if user_input == '1': 
                    user_input = input("1: Schedule Personal Training Session\n"
                                       "2: Scheduling Group Fitenss Class\n"
                                       "3: Exit"
                                       "\n>>> ")
                    # Schedule Personal Training Session --------
                    if user_input == '1':
                        print()

                    # Scheduling Group Fitenss Class -------- 
                    if user_input == '2':
                        print()
                    
                    # Exit --------
                    if user_input == '3':
                        continue

                # Profile Management --------
                elif user_input == '2':
                    user_input = input("1: Update Fitness Goals\n"
                                       "2: Editing Health Metrics\n"
                                       "3: Editing Personal Information\n"
                                       "4: Exit"
                                       "\n>>> ")
                    # Update Fitness Goals --------
                    if user_input == '1':
                        print()

                    # Editing Health Metrics --------
                    if user_input == '2':
                        print()

                    # Editing Personal Information --------
                    if user_input == '3':
                        print()

                    # Exit --------
                    if user_input == '4':
                        continue
                    
                # DashBoard Display --------
                elif user_input == '3':
                    print()

                # Logout --------
                elif user_input == '4':
                    break


        elif account_type == "trainer":
            while True:
                # Trainer Dashboard --------
                user_input = input("1: Schedule management\n"
                                   "2: Profile management\n"
                                   "3: Member Profile Viewing\n"
                                   "4: Logout"
                                       "\n>>> ")
                
                # Schedule management --------
                if user_input == '1':
                    user_input = input("1: Setting Availibility\n"
                                       "2: Exit"
                                       "\n>>> ")
                    if user_input == '1':
                        print()
                    elif user_input == '2':
                        continue
                    
                # Profile management --------
                elif user_input == '2':
                    user_input = input("TBD")

                # Member Profile Viewing --------
                elif user_input == '3':
                    print()

                # Logout --------
                elif user_input == '4':
                    break


        elif account_type == "admin":
            while True:
                # Admin Dashboard --------
                user_input = input( "1: Room Booking Management\n"
                                    "2: Equipment Maintenance Monitoring\n"
                                    "3: Class Schedule Updating\n"
                                    "4: Billing and Payment Processing\n"
                                    "5: Logout"
                                       "\n>>> ")
                
                # Room Booking Management
                if user_input == '1':
                    user_input = input("1: Setting Availibility\n"
                                       "2: Exit"
                                       "\n>>> ")
                    # Setting Availibility
                    if user_input == '1':
                        print()

                    # Exit
                    elif user_input == '2':
                        continue
                    
                # Equipment Maintenance Monitoring
                elif user_input == '2':
                    user_input = input("TBD")

                # Class Schedule Updating
                elif user_input == '3':
                    print()

                # Billing and Payment Processing
                elif user_input == '4':
                    print()

                # Logout
                elif user_input == '5':
                    break


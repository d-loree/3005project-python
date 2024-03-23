import psycopg2
import os
from dotenv import load_dotenv
import sys
from account_management import create_account, login # account management functions
from members import member_dashboard
from trainers import trainer_dashboard
from admins import admin_dashboard
from user import User


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



current_user = User(None, None, None) # current user object/information
while True:

    if current_user.logged_in != True:
        user_input = input( "1: Create New Account\n"
                            "2: Login\n"
                            "3: Quit\n"
                            ">>> ")
        # Create New Account --------
        if user_input == '1':
            try:
                create_account(cursor)
                conn.commit()
            except Exception as error:
                print("\nERROR: ", error)
                conn.rollback()    
        # Login --------
        elif user_input == '2':
            try:
                current_user = login(cursor)
            except Exception as error:
                print("\nERROR: ", error)
        # Quit --------
        elif user_input == '3':
            cursor.close()
            conn.close()
            sys.exit()

    else:
        #if account type is user, display user functions, same for trainer, admin

        if current_user.account_type == "member":
            current_user = member_dashboard(current_user, cursor, conn)


        elif current_user.account_type == "trainer":
            current_user = trainer_dashboard(current_user, cursor, conn)


        elif current_user.account_type == "admin":
            current_user = admin_dashboard(current_user)


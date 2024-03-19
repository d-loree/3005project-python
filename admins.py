from user import User

def admin_dashboard(current_user):
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
                return User(None, None, None)
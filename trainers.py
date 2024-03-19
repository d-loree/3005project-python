from user import User

def trainer_dashboard(current_user):
        while True:
            # Trainer Dashboard --------
            user_input = input("1: Schedule management\n"
                                "2: Profile management\n"
                                "3: Member Profile Viewing\n"
                                "4: Logout"
                                    "\n>>> ")
            
            # Schedule management --------
            if user_input == '1':
                user_input = input("1: Setting Availability\n"
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
                return User(None, None, None)
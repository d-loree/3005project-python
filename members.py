from user import User

def member_dashboard(current_user):
    while True:
        # Member Dashboard --------
        user_input = input("1: Schedule Management\n"
                            "2: Profile Management\n"
                            "3: Dashboard Display\n"
                            "4: Logout\n"
                            ">>> ")
        
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
            return User(None, None, None)
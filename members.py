from user import User
from account_management import update_goal_weight, update_height, update_weight, update_name, update_password, update_email

def member_dashboard(current_user, cursor, conn):
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
                                "2: Scheduling Group Fitness Class\n"
                                "3: Exit"
                                "\n>>> ")
            # Schedule Personal Training Session --------
            if user_input == '1':
                print()

            # Scheduling Group Fitness Class -------- 
            if user_input == '2':
                print()
            
            # Exit --------
            if user_input == '3':
                continue

        # Profile Management --------
        elif user_input == '2':
            user_input = input("\n1: Update Goal Weight\n"
                                "2: Update Weight\n"
                                "3: Update Height\n"
                                "4: Update Name\n"
                                "5: Update Password\n"
                                "6: Update Email\n"
                                "7: Exit"
                                "\n>>> ")
            # Update Goal Weight --------
            if user_input == '1':
                update_goal_weight(current_user, cursor, conn)

            # Update Weight --------
            if user_input == '2':
                update_weight(current_user, cursor, conn)

            # Update Height --------
            if user_input == '3':
                update_height(current_user, cursor, conn)

            # Update Name --------
            if user_input == '4':
                update_name(current_user, cursor, conn)

            # Update password  --------
            if user_input == '5':
                update_password(current_user, cursor, conn)

            # Update Email --------
            if user_input == '6':
                update_email(current_user, cursor, conn)

            # Exit --------
            if user_input == '7':
                continue
            
        # DashBoard Display --------
        elif user_input == '3':
            print()

        # Logout --------
        elif user_input == '4':
            return User(None, None, None)
        





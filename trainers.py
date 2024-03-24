from user import User
from trainer_availability_management import review_current_availability, add_availability, remove_availability

def trainer_dashboard(current_user, cursor, conn):
        while True:
            # Trainer Dashboard --------
            user_input = input("1: Schedule management\n"
                                "2: Member Profile Viewing\n"
                                "3: Logout"
                                    "\n>>> ")
            
            # Schedule management --------
            if user_input == '1':
                user_input = input("1: Review Current availability\n"
                                   "2: Add Availability\n"
                                   "3: Remove Availability\n"
                                    "4: Exit"
                                    "\n>>> ")
                if user_input == '1':
                    review_current_availability(current_user, cursor)

                elif user_input == '2':
                    add_availability(current_user, cursor, conn)
                          
                elif user_input == '3':
                    remove_availability(current_user, cursor, conn)

                elif user_input == '4':
                    continue

            # Member Profile Viewing --------
            elif user_input == '2':
                first_name = input("Enter members first name to search: ")
                last_name = input("Enter members last name to search: ")
                cursor.execute("SELECT first_name, last_name, email, goal_weight, goal_deadline, height, weight "
                               "FROM users JOIN members ON users.id = members.member_id "
                               "WHERE first_name = %s AND last_name = %s;", (first_name, last_name))
                results = cursor.fetchall()
                print(f"\nResults for {first_name} {last_name}:")
                print("-" * 30)
                for record in results:
                    print(f"{record[0]} {record[1]} \nEmail: {record[2]}"
                          f"\nGoal Weight: {record[3]}, Goal Deadline: {record[4]} \nHeight: {record[5]}, Weight: {record[6]}")
                    print("-" * 30)

            # Logout --------
            elif user_input == '3':
                return User(None, None, None)
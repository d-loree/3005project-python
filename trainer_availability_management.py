import re

# TODO: Add try/except blocks

def review_current_availability(current_user, cursor):
    cursor.execute("SELECT * FROM trainer_availability WHERE trainer_id = %s", (current_user.user_id,))
    results = cursor.fetchall()
    print("\nYour current availability:")
    print("-" * 30)
    for result in results:
        print(f"Weekday: {result[2]}\n"
                f"Start Time: {result[3]}\n"
                f"End Time: {result[4]}")
        print("-" * 30)

def add_availability(current_user, cursor, conn):
    day = get_valid_day("Enter day of the week to add availability: ")
    start_time = get_valid_time("start")
    end_time = get_valid_time("end")
    cursor.execute("INSERT INTO trainer_availability (trainer_id, day_of_the_week, start_time, end_time) VALUES (%s, %s, %s, %s);"
                    , (current_user.user_id, day, start_time, end_time))
    conn.commit()
    print("Successfully added availability!")

def remove_availability(current_user, cursor, conn):
    day_to_remove = get_valid_day("What day of the week would you like to clear all availability?: ")
    cursor.execute("DELETE FROM trainer_availability WHERE trainer_id = %s AND day_of_the_week = %s"
                    , (current_user.user_id, day_to_remove))
    conn.commit()
    print(f"Successfully removed all availability on {day_to_remove}s")


def get_valid_day(msg):
    days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input(msg).lower()
        if (day in days_of_the_week):
            return day
        print("Error: That is not a valid day of the week.")

def get_valid_time(start_or_end):
    date_check = r"^(0[0-9]|1[0-9]|2[0-3])\:(0[0-9]|[1-5][0-9])\:(0[0-9]|[1-5][0-9])$"
    while True:
        time = input(f"Enter {start_or_end} time in the format HH:MM:SS (24 hour clock): ")
        if re.match(date_check, time):
            return time
        print("Error: Not a valid time or wrong time format (HH:MM:SS).")
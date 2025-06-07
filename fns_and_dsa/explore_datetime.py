import datetime



def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")


display_current_datetime()



def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days)
    formatted_datetime = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_datetime)

calculate_future_date()

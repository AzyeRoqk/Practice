import time
military_time_hour = int(input("Enter the time in 24-hour format (e.g., 13 for 1 PM): "))
military_time_minute = int(input("Enter the minutes: "))
if military_time_hour > 12:
    military_time_hour = military_time_hour - 12
    print(f" Its {military_time_hour}:{military_time_minute} PM")
elif military_time_hour == 12:
    print(f"It's {military_time_hour}:{military_time_minute} PM")
elif military_time_hour < 12:
    print(f"It's {military_time_hour}:{military_time_minute} AM")
elif military_time_minute > 60:
    print("Oops, you have entered and invalid minute")


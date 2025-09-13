def military_time_to_standard_time (hour, minute):
    if hour > 12:
        hour -= 12
        return f" Its {hour}:{minute} PM"
    elif hour == 12:
        return f" Its {hour}:{minute} PM"
    elif hour < 12:
        return f" It's {hour}:{minute} AM"
def standard_time_to_military_time (hour, minute, period):
    if period == "AM":
        if hour == 12:
            hour = 0
            return f" Its {hour}:{minute} AM"
        elif hour != 12:
            return f" Its {hour}:{minute} AM"
    elif period == "PM":
        if hour == 12:
            hour = 23
            return f" Its {hour}:{minute} PM"
        elif hour != 12:
            hour += 12
            return f" Its {hour}:{minute} PM"

choice = int(input("Choose conversion type: 1 for Military to Standard, 2 for Standard to Military: "))
if choice == 1:
    hour = int(input("Enter hour in 24-hour format: "))
    minute = int(input("Enter minutes: "))
    print (military_time_to_standard_time(hour, minute))
    if minute > 60:
        print("Thats not a valid minute")

elif choice == 2:
    hour = int(input("Enter hour in 12-hour format: "))
    minute = int(input("Enter minutes: "))
    period = input("Enter AM or PM: ").upper()
    print(standard_time_to_military_time(hour, minute, period))
else:
    print("Thats an invalid choice")







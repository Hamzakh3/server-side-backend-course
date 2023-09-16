# Write a Python program that uses the date module to print the current date in the format "YYYY-MM-DD".

# Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".

# Write a program that takes a birth year as input and calculates the age of a person.

# Create a program that calculates and prints the number of days remaining until a person's next birthday.

# Write a program that calculates and displays the number of days between two given dates.

# Create a program that takes a date as string and returns the corresponding day of the week (e.g., Monday, Tuesday, etc.).

# Create a program that takes a year and a month as input and prints the number of days in that month.
# without using calender module

# Create a function that takes a starting date and a number of days as input, and then calculates and prints the date that is the specified number of days in the future.

# Write a Python program that uses the datetime module to print the current date and time.

# Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".

# Create a function that takes a datetime in the format "MM/DD/YYYY HH:MM:SS" as string  formats it as "YYYY-MM-DD HH:MM:SS".

# Write a program that calculates the time difference between two given datetime objects and displays it in hours, minutes, and seconds.

# Create a function that takes a datetime object and a number of hours as input, then returns a new datetime object with the added hours.

# Write a program that takes a date string in the format "MM-DD-YYYY" as input and converts it to a datetime object using strptime().

# Create a function that takes a datetime object as input and formats it as "Month Day, Year" (e.g., "August 25, 2023") using strftime().

# Create a function that takes a datetime object as input and formats it as "Day-Month-Year" (e.g., "25-August-2023") using strftime().

# create a datetime object from the string "26-08-2023 15:18:33.983780-07:00"
# hint: https://strftime.org/

# create a datetime object from the string "08-26-2023 08:10:00 PM"
# hint: https://strftime.org/

# create a datetime object from the string "08-26-2023 08:10:00 PM"
# hint: https://strftime.org/

# dt_named_and_short_form_format = "8-August-23 08:10:00"
# hint: https://strftime.org/

# create a current datetime and then displays it in the format "HH:MM AM/PM"

# Write a program that takes a user-entered date in the format "MM/DD/YYYY" and prints it in the format "YYYY-MM-DD".

# Create a function that takes a datetime object as input and displays the day of the week (e.g., "Monday") using strftime().
# hint: https://strftime.org/

# Create a function that takes a timezone name as input and prints the current date time object in that timezone.

# Write a program that converts a given date time (tz aware) string from one timezone to another.

# Write a program that takes a datetime object (naive) and a timezone name as input, and returns a localized datetime object in the specified timezone.

# Create a function that takes a timezone name and a number of hours as input, and prints the current time plus the specified hours in that timezone

# Write a program that calculates the date and time of the daylight saving start in the year 2022.
# take timezone "US/Pacific"
# take string date as "2022-01-01 00:00:00"
# hint: use
# bool(tz_aware_dt.dst()) == True # dst activated
# bool(tz_aware_dt.dst()) == False # dst not activated


# Write a program that calculates the date and time of the daylight saving end in the year 2022.
# take timezone "US/Pacific"
# take string date as "2022-01-01 00:00:00"
# hint: use
# bool(tz_aware_dt.dst()) == True # dst activated
# bool(tz_aware_dt.dst()) == False # dst not activated

# Design a program that helps schedule a meeting across different timezones. The program should take the meeting time in one timezone and display the corresponding times in other timezones.
# consider three countries: UK, US, Saudi Arab and Pakistan
# consider the meeting time is: 30 August 2023 at 2 PM Pakistan time


# Booking System
# Design a booking system where users specify a start datetime, end datetime, and timezone.
# Implement a function that checks whether a specified time slot is available.
# if timeslot is available then store the start_date and end_date in the list of objects i.e
from datetime import timedelta
from datetime import datetime, date, time
import pytz


booking_storage = [
    {
        "start_date": "",
        "end_date": ""
    }
]

for count in range(5):
    start_time = input("Start Time\n")
    end_time = input("End Time\n")
    time_zone = input("Time Zone\n")

    format_start_time = datetime.fromisoformat(start_time)
    format_end_time = datetime.fromisoformat(end_time)
    user_time_zone = pytz.timezone(time_zone)

    tz_aware_start_dt = user_time_zone.localize(format_start_time)
    tz_aware_end_dt = user_time_zone.localize(format_end_time)

    tz_aware_start_dt_utc = tz_aware_start_dt.astimezone(pytz.utc)
    tz_aware_end_dt_utc = tz_aware_end_dt.astimezone(pytz.utc)

    if count == 0:
        booking_storage[count] = {
            "start_date": tz_aware_start_dt_utc,
            "end_date": tz_aware_end_dt_utc
        }
        print("Booking Successfully")
    else:
        booked_start_dt = booking_storage[count - 1]["start_date"]
        booked_end_dt = booking_storage[count - 1]["end_date"]

        if tz_aware_start_dt_utc != booked_start_dt and tz_aware_end_dt_utc != booked_end_dt:
            print("Already Booked")
        
    print(tz_aware_start_dt)
    print(tz_aware_end_dt)
    print(booking_storage)

    # booked_start_time = booking_storage[0]["start_date"]
    # booked_end_time = booking_storage[0]["end_date"]


#
# tz_aware_dt.astimezone(pytz.timezone("Asia/Karachi"))


# hint 1: store dates in booking_storage in UTC format i.e pytz.utc
# hint 2: use for loop, the loop should run 5 times. ask user input inside the loop

# instruction to test your program:
# first iteration of loop
# give input "2023-08-26 18:00:00" as start_date and "2023-08-26 19:00:00" as end_date and "Asia/Karachi" as timezone

# second iteration of loop
# give input "2023-08-26 16:00:00" as start_date and "2023-08-26 17:00:00" as end_date and "Asia/Riyadh" as timezone
# above program should not accept this booking as the slot is already booked by the first iteration


# instruction to test your program:
# first iteration of loop
# give input "2023-08-26 18:00:00" as start_date and "2023-08-26 19:00:00" as end_date and "Asia/Karachi" as timezone

# second iteration of loop
# give input "2023-08-26 16:00:00" as start_date and "2023-08-26 17:00:00" as end_date and "Asia/Riyadh" as timezone
# above program should not accept this booking as the slot is already booked by the first iteration


import pytz
from datetime import datetime

khi_start_date = datetime.fromisoformat("2023-08-26 18:00:00")
khi_end_date = datetime.fromisoformat("2023-08-26 19:00:00")
khi_tz = pytz.timezone("Asia/Karachi")

khi_start_date_tz_aware = khi_tz.localize(khi_start_date)
khi_end_date_tz_aware = khi_tz.localize(khi_end_date)

# print(khi_start_date_tz_aware, khi_end_date_tz_aware)
print("khi start", khi_start_date_tz_aware.astimezone(pytz.utc))
print("khi end", khi_end_date_tz_aware.astimezone(pytz.utc))



ryd_start_date = datetime.fromisoformat("2023-08-26 16:00:00")
ryd_end_date = datetime.fromisoformat("2023-08-26 17:00:00")
ryd_tz = pytz.timezone("Asia/Riyadh")

ryd_start_date_tz_aware = ryd_tz.localize(ryd_start_date)
ryd_end_date_tz_aware = ryd_tz.localize(ryd_end_date)

# print(ryd_start_date_tz_aware, ryd_end_date_tz_aware)

print("ryd start", ryd_start_date_tz_aware.astimezone(pytz.utc))
print("ryd end", ryd_end_date_tz_aware.astimezone(pytz.utc))
	# Booking System
 # Design a booking system where users specify a start datetime, end datetime, and timezone. Implement a function that checks whether a specified time slot is available.
 # if timeslot is available then store the start_date and end_date in the list of objects i.e
 
import pytz
from datetime import datetime
 
booking_storage = [
    {
        "car_model": "",  # corolla, civic

        "start_date": "",
        "end_date": ""
     }
 ]
 
 # hint 1: store dates in booking_storage in UTC format i.e pytz.utc
 # hint 2: use for loop, the loop should run 5 times. ask user input inside the loop
 
 # instruction to test your program:
 # first iteration of loop
 # give input "2023-08-26 18:00:00" as start_date and "2023-08-26 19:00:00" as end_date and "Asia/Karachi" as timezone and car_model
 
 # second iteration of loop
 # give input "2023-08-26 16:00:00" as start_date and "2023-08-26 17:00:00" as end_date and "Asia/Riyadh" as timezone  and car_model
 # above program should not accept this booking as the slot is already booked by the first iteration
 
 # You must write the following functions
 
 # add_tz() # this should convert native date to tz_awre
 # convert_tz() # this should convert date from one tz to another
 # is_slot_available() # this should return True or False
 # book_the_car() # this should add the detail in booking_storage
 
 # I didn't mention what info you need to pass to the above functions.
 # Its part of your assigment to pass info to the function and return the value from function.
 
 
def convert_date_tz_as_user(tz="", start_date_time="", end_date_time=""):
     if tz and start_date_time and end_date_time:
         user_tz = pytz.timezone(tz)
         start_date_time_tz_aware = user_tz.localize(
             datetime.fromisoformat(start_date_time))
         end_date_time_tz_aware = user_tz.localize(
             datetime.fromisoformat(end_date_time))
 
         utc_start_date_time = start_date_time_tz_aware.astimezone(pytz.utc)
         utc_end_date_time = end_date_time_tz_aware.astimezone(pytz.utc)
         return [utc_start_date_time, utc_end_date_time]
 
 
def is_slot_available(start_date, end_date, car):
     for booking in booking_storage:
         booking_sd = booking["start_date"]
         booking_ed = booking["end_date"]
         booking_car = booking["car_model"]
         print(booking_sd, booking_ed, booking_car)
         if booking_sd == start_date and booking_ed == end_date and booking_car == car:
             return False

     print("loop end")
     return True 
 
def book_the_car(date, car_model):
     is_available = is_slot_available(date[0], date[1], car_model)
     if is_available == True:
         print("Booking Confirmed")
         return True
     else:
         print("Already Booked")
         return False
 
 
for count in range(5):
     st_date = input("Start Date")
     en_date = input("End Date")
     time_zone = input("Time Zone")
     car = input("Car Model")
     utc_date = convert_date_tz_as_user(time_zone, st_date, en_date)
     is_booked = book_the_car(utc_date, car)
     if (is_booked == False):
         break
     else:
         detail = {
             "car_model": car,  # corolla, civic
             "start_date": utc_date[0],
             "end_date": utc_date[1]
         }
         booking_storage.append(detail)
  
 
# Date Handle

# Way 1 get module
# import datetime

# Way 2 get module from module
""" 
from datetime import datetime
from datetime import date
from datetime import time
 """

# Way 3 get module from module with comma seperated
from datetime import timedelta
from datetime import datetime, date, time

# Play with current date and time
""" 
current_date = date.today()
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date_time = datetime.now()
print(current_date_time)

print(type(current_date))
print(type(current_date_time))
 """

# create date and time from integer or string

# From INteger
""" 
my_day = 26
my_month = 8
my_year = 2023
d = date(year=my_year, month=my_month, day=my_day)
print(d)
 """
# From ISO 8601
""" 
dt_iso = "2023-08-26" # ISO 8601
dt = "2023-08-26" # not an ISO 8601
dt = "2023-08-26" # not an ISO 8601

dt_obj = date.fromisoformat(dt_iso)
print(dt_obj)

date_time_str = "2023-08-26T10:54:00+05:00" #ISO 8601
date_time_str = "2023-08-26T10:54:00.321Z" #ISO 8601
date_time_str = "2023-08-26T10:54:00Z" #ISO 8601
date_time_str = "2023-08-26T10:54:00" #ISO 8601
date_time_str = "2023-08-26 10:54:00" #ISO 8601
dt_obj = datetime.fromisoformat(date_time_str)
print(dt_obj)
 """

# From TimeStamp
""" 
ts = 1693029240 #timestamp

dt_obj = datetime.fromtimestamp(ts)
print(dt_obj.year)

dt_pk = "26-08-2023"
dt_us = "08/26/2023"
dt_invalid = "26/-08-/2023"
dt_iso= "2023-08-26"

dt = datetime.strptime(
    dt_pk,
    "%d-%m-%Y"
)
print(dt)

dt = datetime.strptime(
    dt_us,
    "%m/%d/%Y"
)
print(dt)

dt = datetime.strptime(
    dt_invalid,
    "%d/-%m-/%Y"
)
print(dt)
 """


# Jesa string data main format hy same define krna ho ga format main
""" 
dt = datetime.now()
x =  str(dt)

dt_obj = datetime.strptime(
    x,
    "%Y-%m-%d %H:%M:%S.%f"
)
print(dt_obj)
 """

#  Date Manipulation
""" 
dt = "2023-01-01 23:59:59"
dt_obj = datetime.fromisoformat(dt)

x = dt_obj.replace(year=2020)
print(x)
x= dt_obj.replace(hour=3)
print(x)

from dateutil import parser #need to install
x = "2023/02/01"
dt_obj = parser.parse(x)
print(dt_obj.month)
 """

#  Date Manipulation using timedelta
""" 
dt = date.today()
x = dt - timedelta(days=2)
print(x)

x = date.fromisoformat("2023-08-05")

for i in range(1, 10):
    change_dt = x - timedelta(days=i)
    # change_dt = x.replace(day=(x.day - i))
    print(change_dt)
     """

# Calculate Difference Between Date
""" 
current_date = datetime.now()
custom_dt = datetime.now()

custom_dt = custom_dt.replace(day=2)
print(custom_dt, current_date)

diff = current_date - custom_dt
diffHours = diff.total_seconds() / (60*60)

print(diffHours)
 """

#  Using Calendar

import calendar
""" 
month_range = calendar.monthrange(2023, 3) #return tupple
print(month_range)
 """

# Use Timezone
import pytz
"""
# Just for Example no need to practice this not a perfect way 
time_zone = pytz.all_timezones
current_dt = datetime.now(tz=pytz.timezone("Asia/Karachi"))

dt_str = "2023-02-03 13:40:00" #US/Pacific
dt_obj = datetime.fromisoformat(dt_str)

dt_obj = dt_obj.replace(tzinfo=pytz.timezone("Asia/Karachi"))
print(dt_obj)
 """

tz_detail = pytz.timezone("US/Pacific")
dt_str = "2020-03-07 13:40:00" #US/Pacific
dt_obj = datetime.fromisoformat(dt_str)

tz_aware_dt = tz_detail.localize(dt_obj)
print(tz_aware_dt)

dt_str = "2020-03-08 13:40:00" #US/Pacific
dt_obj = datetime.fromisoformat(dt_str)

tz_aware_dt = tz_detail.localize(dt_obj)
print(tz_aware_dt)

# 
tz_aware_dt.astimezone(pytz.timezone("Asia/Karachi"))

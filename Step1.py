# Step 1 basic functionality of countdown
# User can write in event and time
# User can see countdown to event

#import datetime
from datetime import *
import time

#Global variables for converting time from seconds
SECONDS = 60 # seconds in a minute
MINUTES = SECONDS * 60 #seconds in an hour
HOURS = MINUTES * 24 # hours in a day
DAYS = HOURS * 24


#enter event and date time

#event_desc = input("Enter event name: ")
#time_string = input ("Date and time for event (dd/mm/yyyy hh:mm): ")

event_desc = "test"
time_string = "23/06/2021 13:40"

#calculate time remaining in seconds
event_time = datetime.strptime(time_string, "%d/%m/%Y %H:%M")
remaining_time = event_time - datetime.now()

print("Event time is {0:s}".format(event_time.strftime("%d/%m/%Y %H:%M:%S")))
print()
print()
#Time remaining in seconds
countdown = int(remaining_time.total_seconds())

#print("\n{0:s}".format(after1.strftime("%d %H:%M:%S")))
print("countdown in seconds", countdown)


#Seperate countdown seconds into units days, hours, minutes, seconds
seconds = countdown % SECONDS
minutes = (countdown // SECONDS) % SECONDS
hours = (countdown // MINUTES) % 24
days = (countdown // HOURS)

print("Days is: ", days)
print("Hours is: ", hours)
print("Minutes is: ", minutes)
print("Seconds is: ", seconds)
print()
print("Remaining Time is: ", remaining_time) 




print("\nend")


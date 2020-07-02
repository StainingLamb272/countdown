# Step 1 basic functionality of countdown
# User can write in event and time
# User can see countdown to event
# Step 2 run and display countdown

#import datetime
from datetime import *
import time

#Global variables for converting time from seconds
SECONDS = 60 # seconds in a minute
MINUTES = SECONDS * 60 #minutes in an hour
HOURS = MINUTES * 24 # hours in a day
DAYS = HOURS * 24


#enter event and date time

#event_desc = input("Enter event name: ")
#time_string = input ("Date and time for event (dd/mm/yyyy hh:mm): ")

event_desc = "test"
time_string = "22/06/2020 12:12"

#calculate time remaining in seconds
event_time = datetime.strptime(time_string, "%d/%m/%Y %H:%M")
remaining_time = event_time - datetime.now()

print("Event time is {0:s}".format(event_time.strftime("%d/%m/%Y %H:%M:%S")))
print()
print()
#Time remaining in seconds
countdown = int(remaining_time.total_seconds())


#Seperate countdown seconds into units days, hours, minutes, seconds
seconds = countdown % SECONDS
minutes = (countdown // SECONDS) % SECONDS
hours = (countdown // MINUTES) % 24
days = (countdown // HOURS)

#Test countdown 5 seconds 
print("\nDays   Hours   Min   Sec")
'''
for i in range(15):   
    
    print(f"{days}  {hours}  {minutes}  {seconds}")
    seconds -= 1
    time.sleep(1)
'''
# initiate flags for end of countdown

day0 = False
hour0 = False
minute0 = False


first_time = True #flag 1st time in countdown loop

#*************Display countdown**************************

print(f"{days}  {hours}  {minutes}  {seconds}")
#Run off remaining seconds in current minute
'''while seconds >= 0:
    print('{0:3d} {1:6d} {2:6d} {3:5d}'.format(days, hours, minutes, seconds))
    time.sleep(1)
    seconds -= 1'''
#Start here if countdown > 60 seconds????

while not day0 and not hour0 and not minute0 and seconds > 0: #???????? #While not finished
    #Transfer remaing values from big unit to small (1 min to 59sec)
    while days >= 0 and not day0:
        if not first_time: #don't chage 1st time
            if days > 0: #and #not first_time: 
                days -= 1
                hours = 23
                hour0 = False
            else:
                day0 = True
        while hours >= 0 and not hour0:
            if not first_time:
                if hours > 0: #and not first_time:
                    hours -= 1
                    minutes = 59
                    minute0 = False
                else:
                    hour0 = True
            while minutes >= 0 and not minute0:
                if not first_time:
                    if minutes > 0: #and not first_time:
                        minutes -= 1
                        seconds = 59
                    else:
                        minute0 = True
                while seconds >= 0:
                    first_time = False
                    print('{0:3d} {1:6d} {2:6d} {3:5d}'.format(days, hours, minutes, seconds))
                    #time.sleep(1)
                    #seconds -= 1
                    #Speed test hour
                    time.sleep(0.5)
                    seconds -= 120

print("\nend")


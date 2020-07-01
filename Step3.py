
# Step 3 lag event class

#import datetime
from datetime import *
import time

SECONDS = 60 # seconds in a minute
MINUTES = SECONDS * 60 #minutes in an hour
HOURS = MINUTES * 24 # hours in a day

class Event:
    def __init__(this, name, time):
        this.__name = name
        this.__time = datetime.strptime(time, "%d/%m/%Y %H:%M")

    def get_name(this):
        return this.__name

    def set_name(this, name):
        this.__name = name

    def set_time(this, time):
        this.__time = time

    def get_time(this):
        return this.__time

    def __str__(this): #custom string
        return "Event name {0:s} \nEvent time {1:s}".format(this.__name, str(this.__time))


def remaining_time_seconds(event_time):
    remaining_time = event_time - datetime.now()
    countdown = int(remaining_time.total_seconds())
    return countdown

#Seperate countdown seconds into units days, hours, minutes, seconds
def remaining_seconds(countdown):
    seconds = countdown % SECONDS
    return seconds

def remaining_minutes(countdown):
    minutes = (countdown // SECONDS) % SECONDS
    return minutes

def remaining_hours(countdown):
    hours = (countdown // MINUTES) % 24
    return hours

def remaining_days(countdown):
    days = (countdown // HOURS)
    return days



def display_countdown(countdown):

    seconds = remaining_seconds(countdown)
    minutes = remaining_minutes(countdown)
    hours = remaining_hours(countdown)
    days = remaining_days(countdown)
    
    # initiate flags for end of countdown
    day0 = False
    hour0 = False
    minute0 = False

    first_time = True #Flag 1st time in countdown loop - Don't change 1st time

    while not day0 and not hour0 and not minute0 and seconds > 0: #While not finished
    #Transfer remaing values from big unit to small (1 min to 59sec etc.)
        while days >= 0 and not day0:
            if not first_time:
                if days > 0:
                    days -= 1
                    hours = 23
                    hour0 = False
                else:
                    day0 = True
            while hours >= 0 and not hour0:
                if not first_time:
                    if hours > 0:
                        hours -= 1
                        minutes = 59
                        minute0 = False
                    else:
                        hour0 = True
                while minutes >= 0 and not minute0:
                    if not first_time:
                        if minutes > 0:
                            minutes -= 1
                            seconds = 59
                        else:
                            minute0 = True
                    while seconds >= 0:
                        first_time = False
                        print('{0:3d} {1:6d} {2:6d} {3:5d}'.format(days, hours, minutes, seconds))
                        time.sleep(1)
                        seconds -= 1
                        



def main():
    #enter event and date time
    event_desc = input("Enter event name: ")
    time_string = input ("Date and time for event (dd/mm/yyyy hh:mm): ")

    #create event object
    my_event = Event(event_desc, time_string)

    print(my_event)
    print()


    countdown = remaining_time_seconds(my_event.get_time())
    print(countdown)

    print()

    display_countdown(countdown)

    print()
    


main()

#End of program

    

    

    


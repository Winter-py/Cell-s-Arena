#Countdown Timer Project
import datetime
import time 


countdown_time = datetime.datetime.now() + datetime.timedelta(days=1)

def countdown(countdown_time):
    while True:
        now = datetime.datetime.now()
        if now > countdown_time:
            print("Time's up!")
            break
        else:
            time_left = countdown_time - now
            print(time_left)
            time.sleep(1)


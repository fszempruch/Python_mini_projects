### Countdown
import datetime
import time
from playsound import playsound


def time_diff(date_to):
    diff = date_to - datetime.datetime.now()
    days_diff = diff.days
    hours_diff = diff.seconds // 3600
    minutes_diff = (diff.seconds % 3600) // 60
    seconds_diff = diff.seconds % 60
    return diff, days_diff, hours_diff, minutes_diff, seconds_diff


date_to = input(
    "Enter the date for which the difference is to be counted in YYYY-MM-DD HH:MM:SS format: "
)

try:
    date_to = datetime.datetime.strptime(date_to, "%Y-%m-%d %H:%M:%S")
except:
    print("Wrong date format!")
else:
    if date_to <= datetime.datetime.now():
        print(
            "Its impossible to countdown, because given date and time is earlier than current date and time."
        )
    else:
        print("Counting down to: ", date_to)

        while True:
            diff, days_diff, hours_diff, minutes_diff, seconds_diff = time_diff(date_to)

            if days_diff < 0:
                print("Countdown finished!")
                playsound(
                    "C:/Users/Filip/Desktop/Projekty/Python_mini_projects/Countown/gong.wav"
                )
                break
            else:
                print(
                    f"Days left: {days_diff}, Hours left: {hours_diff}, Minutes left: {minutes_diff}, Seconds left: {str(seconds_diff).zfill(2)}",
                    end="\r",
                )
            time.sleep(1)

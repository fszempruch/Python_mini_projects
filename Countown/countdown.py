### Countdown
import datetime
import time
from playsound import playsound


def time_diff(date):
    diff = date - datetime.datetime.now()
    days_diff = diff.days
    hours_diff = diff.seconds // 3600
    minutes_diff = (diff.seconds % 3600) // 60
    seconds_diff = diff.seconds % 60
    return days_diff, hours_diff, minutes_diff, seconds_diff


def validate_date(date, format="%Y-%m-%d %H:%M:%S"):
    try:
        date = datetime.datetime.strptime(date, format)
    except:
        print("Wrong date format!")
    else:
        if date <= datetime.datetime.now():
            print(
                "Its impossible to countdown, because given date is earlier than current date"
            )
        else:
            return date


def clear_console_last_line():
    print("\033[A" + " " * 62 + "\033[A")


def countdown():
    date_to = []

    while isinstance(date_to, datetime.datetime) != True:
        date_input = input(
            "Enter the date for which the difference is to be counted in YYYY-MM-DD HH:MM:SS format: "
        )
        date_to = validate_date(date_input)

    print("Counting down to: ", date_to)

    while True:
        days_diff, hours_diff, minutes_diff, seconds_diff = time_diff(date_to)

        if days_diff < 0:
            print("Countdown finished!")
            playsound(
                "C:/Users/Filip/Desktop/Projekty/Python_mini_projects/Countown/gong.wav"
            )
            break
        else:
            print(
                f"Days left: {days_diff}, Hours left: {hours_diff}, Minutes left: {minutes_diff}, Seconds left: {seconds_diff}"
            )
        time.sleep(1)
        clear_console_last_line()


if __name__ == "__main__":
    countdown()

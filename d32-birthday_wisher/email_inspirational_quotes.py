import smtplib
import datetime as dt
import random

day = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# get a random quote of the day
with open("quotes.txt", "r") as file:
    quotes = file.readlines()
quote = random.choice(quotes)

# set some defaults for the send_email function
from_email = ""
to_email = ""
GOOGLE_SMTP = ""
YAHOO_SMTP = ""
password = ""


def send_mail(from_email, to_email, subject, message, **kwargs):
    with smtplib.SMTP(GOOGLE_SMTP, port=587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n{message}"
        )


# # create custom datetime object
# date_of_birth = dt.datetime(year=1970, month=10, day=1)
# print(date_of_birth)

# work with the current time
now = dt.datetime.now()
# year = now.year
# month = now.month
day_of_week = now.day
if day_of_week == 6:
    today = day[day_of_week - 1]
    subject = f"Inspirational quote for {today}"
    message = (f"Your Inspirational Quote of the day: \n{quote}")
    print(message)

    send_mail(from_email, to_email, subject, message)

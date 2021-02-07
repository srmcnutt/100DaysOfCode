#  100 days of code day 32 - birthday wisher
import datetime as dt
import pandas as pd
import random
import smtplib
import os
import csv

# set some defaults for the send_email function
# use export FROM_EMAIL="myemail@.mydomain.com"
# and export EMAIL_CREDS="mycreds"
# to set from address and email password
# never store these in the program.
from_email = os.environ.get("FROM_EMAIL")
password = os.environ.get("EMAIL_CREDS")
subject = "happy Birthday from Steve!"
GOOGLE_SMTP = "smtp.gmail.com"
YAHOO_SMTP = "smtp.mail.yahoo.com"


def send_mail(**kwargs):
    with smtplib.SMTP(GOOGLE_SMTP, port=587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n{message}",
        )


# set up some variables
now = dt.datetime.now()
today = (now.month, now.day)
letter_path = "letter_templates/"

# Pandas way
# read the birthdays.csv
data = pd.read_csv("birthdays.csv")

# check for month and day match
birthdays_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()
}


print(birthdays_dict)


if today in birthdays_dict:
    letter_file = f"{letter_path}letter_{random.randint(1,3)}.txt"
    with open(letter_file, "r") as file:
        letter = file.read()
    to_email = birthdays_dict[today]["email"]
    message = letter.replace("[NAME]", birthdays_dict[today]["name"])
    print(message)
    send_mail()

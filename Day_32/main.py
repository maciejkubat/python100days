import smtplib
import datetime as dt
from random import choice

def send_mail(message):
   my_email = "maciek.kubat@gmail.com"
   password = ""
   with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
       connection.starttls()
       connection.login(user=my_email,password=password)
       connection.sendmail(
           from_addr=my_email,
           to_addrs=my_email,
           msg=f"Subject:Quote for monday\n\n{message}"
       )

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt") as file:
    quotes = file.readlines()
quote = choice(quotes)

if day_of_week == 1:
    send_mail(quote)
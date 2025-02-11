##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
from random import choice
import pandas as p

file_names = ["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]
now = dt.datetime.now()
data = p.read_csv('birthdays.csv')
templates = []

def send_mail(message, to_address):
   my_email = "maciek.kubat@gmail.com"
   password = "ryiu gzhj puxp aklp"
   with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
       connection.starttls()
       connection.login(user=my_email,password=password)
       connection.sendmail(
           from_addr=my_email,
           to_addrs=to_address,
           msg=f"Subject:Happy birthday\n\n{message}"
       )

for filename in file_names:
    with open(filename) as file:
        templates.append(file.read())

for (index, row) in data.iterrows():
    if row.month == now.month and row.day == now.day:
        print(row.full_name)
        template = choice(templates)
        content = template.replace("[NAME]",f"{row.full_name}")
        send_mail(message=content,to_address=row.email)
        print(f"Email sent to: {row.full_name}")


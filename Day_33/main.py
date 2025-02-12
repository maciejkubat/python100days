from operator import truediv
import smtplib
from time import sleep

import requests
from datetime import datetime

MY_LAT = 50.073727
MY_LONG = 19.917954

def send_mail(message):
   my_email = "maciek.kubat@gmail.com"
   password = ""
   with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
       connection.starttls()
       connection.login(user=my_email,password=password)
       connection.sendmail(
           from_addr=my_email,
           to_addrs=my_email,
           msg=f"Subject:ISS\n\nIss is over you and it is dark"
       )


def is_iss_overhead(lat, long):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    long_range = (iss_longitude - 5 , iss_longitude + 5)
    lat_range = (iss_latitude - 5, iss_latitude + 5)
    if long_range[0] < long < lat_range[1] and lat_range[0] < lat < lat_range[1]:
        return True
    else:
        return False

def is_it_dark():
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted" : 0
    }
    response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now= datetime.now().hour
    if time_now > sunset or time_now < sunrise:
        return True
    else:
        return False

while True:
    if is_iss_overhead(lat=MY_LAT, long=MY_LONG) and is_it_dark():
        print("ISS is over you and it is dark")
        send_mail()
    else:
        print("Sorry")
    sleep(60)
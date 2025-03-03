from idlelib.iomenu import encoding

from bs4 import BeautifulSoup
import requests
import smtplib
import os
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

TARGET_PRICE = 100
LINK = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

def send_mail(message):
   my_email = "maciek.kubat@gmail.com"
   password = os.environ.get("PASS")
   # Create a multipart message
   msg = MIMEMultipart()
   msg['From'] = my_email
   msg['To'] = my_email
   msg['Subject'] = "Price Alert"

   # Attach the message body with UTF-8 encoding
   msg.attach(MIMEText(message, 'plain', 'utf-8'))

   with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
       connection.starttls()
       connection.login(user=my_email,password=password)
       connection.sendmail(
           from_addr=my_email,
           to_addrs=my_email,
           msg=msg.as_string(),
       )
def get_current_price(link=LINK):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
              "Language" : "en-US"}
    response = requests.get(link, headers=header, verify=False)

    amazon_webpage = response.text
    soup = BeautifulSoup(amazon_webpage, "html.parser")
    print(soup.prettify())

    price_whole = soup.find(name="span", class_="a-price-whole").getText().split(".")[0]
    price_fraction = soup.find(name="span", class_="a-price-whole").getText().split(".")[0]
    current_price = float(f"{price_whole}.{price_fraction}")
    return current_price

def get_product_name(link=LINK):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
    response = requests.get(link, headers=header, verify=False)

    amazon_webpage = response.text
    soup = BeautifulSoup(amazon_webpage, "html.parser")
    product_name = soup.find(name="h1", id="title").getText().strip()
    return product_name


if get_current_price() < TARGET_PRICE:
    name = re.sub(r'\s+', ' ', get_product_name())
    print(name)
    price = get_current_price()
    send_mail(f"{name} is now {price} \n Get it here {LINK}")
import requests
from datetime import datetime
from time import sleep
from replit import clear
import smtplib

MY_LAT = -0 
MY_LONG = -0
FORM = 0
RUNNING = True
#--------------------------------------------------------------------------- 
USERNAME = "email@gmail.com"
PASSWORD = "sdsdsdsd"

# -------------------------- Space Station api data ------------------------#
def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

# -------------------------- Sunrise, sunset api data ----------------------#
def is_night():
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted": FORM,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 3
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 3
    
    time_now = datetime.now()
    time_hour = time_now.hour
    if time_hour >= sunset or time_hour <= sunrise:
        return True   
while RUNNING:
    print("Waiting for...")
    sleep(60)
    clear()
    if is_night() and is_iss_close():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD)
            connection.sendmail(from_addr=USERNAME, to_addrs=USERNAME, msg="Subject: Look up 👆\n\nLook up the ISS is above you in the sky.")
            print("Successful!! Email sent.")
            RUNNING = False
    else:
        print("Wait for ISS to appear close to you in the right time.")
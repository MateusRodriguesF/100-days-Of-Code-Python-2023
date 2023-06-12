# import smtplib
# my_email = "email@gmail.com"
# my_password = "sdsdsd"
# dest_email = "email@hotmail.com"
# email_msg = "Subject:Hello\n\nThis is a test email."
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,to_addrs=dest_email, msg=email_msg)

# import datetime as dt0
# now = dt.datetime.now()
# year = now.year
# month = now.month
# week_day = now.weekday()
# print(month)
# date_of_birth = dt.datetime(year=1990, month=8, day=13)
# print(date_of_birth)

# ------------------------ Motivational mail sender ----------------------------- #

# --------------------------- Begin ----------------------------------------------#
import datetime as dt
import smtplib
import random
import time

def send_mail(msg):
    my_email = "email.t@gmail.com"
    my_password = "sdsdsd"
    dest_email = "email@hotmail.com"
    email_msg = f"Subject:Motivational quote of the day\n\n{msg}"
    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs=dest_email, msg=email_msg)
#----------------------------- Picking a random quote -----------------------------#
with open(r"Day_32\quotes.txt") as quotes_file:
    quotes = [line.rstrip() for line in quotes_file.readlines()]# txt to a list in one line
rnd_qut = random.choice(quotes)

#----------------------------- date -----------------------------#
now = dt.datetime.now()
day = now.weekday()

if day == 2:
    print(f"Today is Wednesday\nDay of Motivational Quote:\n{rnd_qut}")
    print("Sending this message to e-mail")
    time.sleep(1)
    send_mail(rnd_qut)

# ----------------------------- End ------------------------------ #
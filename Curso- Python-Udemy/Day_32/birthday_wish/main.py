from datetime import datetime
import pandas as pd
import smtplib
import random
#------------------------ Var & Const ------------------------#
USERNAME = "email@gmail.com"
PASSWORD = "dsdsdsdsdsdsd"
#------------------------ Datetime ------------------------#
today = datetime.now()
today_tuple = (today.month, today.day)
# print(today_tuple)
#------------------------ reading file ------------------------#
birth_data = pd.read_csv(r"Day_32\birthday_wish\birthdays.csv") 
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birth_data.iterrows()}
# print(birthdays_dict)
#------------------------ Logic ------------------------#
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = fr"Day_32\birthday_wish\letter_templates\letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_template:
        content = letter_template.read()
        contents = content.replace("[NAME]", birthday_person["name"])
        # print(content)
        print(birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(from_addr=USERNAME, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")
        print("Sent mail")

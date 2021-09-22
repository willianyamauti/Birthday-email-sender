import smtplib
import random
import datetime as dt
import pandas as pd

# fill your data here
YOUR_NAME = 'John'
my_email = "johndoe@gmail.com"
password = 'xxxxxxxxxxxxxxx'
smtp = "smtp.gmail.com"

now = dt.datetime.now()
now_tuple = (now.month, now.day)
birthdays_list = pd.read_csv('birthdays.csv')
bd_database = [{(data_row["month"], data_row["day"]): data_row} for (index, data_row) in birthdays_list.iterrows()]
# filter database for every birthday that matches today
filtered_database = filter(lambda bd: now_tuple in bd, bd_database)

for person in filtered_database:
    person = person[now_tuple]
    with smtplib.SMTP(smtp) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        with open(f'letter_templates/letter_{random.randint(1,3)}.txt', 'r') as templates:
            letter = templates.read()
            letter = letter.replace("[NAME]", person["name"])
            letter = letter.replace("[YOU]", YOUR_NAME)
            connection.sendmail(from_addr=my_email,
                                to_addrs=person['email'],
                                msg=f'Subject:Happy Birthday!!!!\n\n{letter}')







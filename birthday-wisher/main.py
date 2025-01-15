import pandas
import smtplib
import datetime as dt
from person import Person
from random import randint

# 1. Update the birthdays.csv
df = pandas.read_csv("birthdays.csv")

persons = [
    Person(name=row.name, email=row.email, day=row.day, month=row.month)
    for row in df.itertuples(index=False)
]

my_email = "shmobbob70@gmail.com"
app_password2 = "SOME_PASSWORD_HERE"

def send_motivation(motivation):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, app_password2)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="bobshmob70@yahoo.com",
            msg=f"Subject: Happy birthday!\n\n{motivation}")

now = dt.datetime.now()

for person in persons:
    if now.day == person.day and now.month == person.month:
        with open(f"letter_templates/letter_{randint(1,3)}.txt", mode="r") as random_letter:
            content = random_letter.read()
            content = content.replace("[NAME]", person.name)
            print(content)
            send_motivation(content)





import datetime as dt
import pandas
import random
import smtplib

# ToDO 1. Update the birthdays.csv
# Done

# ToDO 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
this_month = now.month
today = now.day

data = pandas.read_csv("birthdays.csv")
birthdays_list = data.to_dict(orient="records")

is_birthday = [person for person in birthdays_list
               if this_month == person['month'] and today == person['day']]

# ToDo 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
#  actual name from birthdays.csv
if is_birthday:
    for person in is_birthday:
        letter_num = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_num}.txt") as birthday_letter:
            letter = birthday_letter.read()
            modified_letter = letter.replace("[NAME]", person['name'])

        # ToDO 4. Send the letter generated in step 3 to that person's email address.
        my_email = "pythontest32288@gmail.com"
        my_password = "gsrfzucledwimgqp"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=person['email'],
                                msg=f"Subject: Happy Birthday!\n\n{modified_letter}")

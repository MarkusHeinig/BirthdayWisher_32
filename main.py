from random import choice
import smtplib
import datetime as dt

my_email = "...@gmail.com"
password = "..."

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as t:
        quotes = t.readlines()
        random_quote = choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        # TLS = transport layer security - content encryption
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="...@yahoo.com",
            msg=f"Subject:Motivational Quote\n\n{random_quote}"
        )
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = dt.datetime.now().month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)

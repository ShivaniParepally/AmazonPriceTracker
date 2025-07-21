# import datetime
import time
import schedule
from extract_price import findPrice
#from extract_price import url
from smtp import sendEmail
import pandas as pd
import csv

#name= input("Enter recipient name: ") # must actually get this from html frontend
#recipient_email = input("Enter recipient's mail id: ") # must get this from html frontend

# def read_csv(file_name):
#     return pd.read_csv(file_name)


def check():
    with open('storage.csv','r') as csvfile:
        csv_reader = list(csv.DictReader(csvfile))
        

        for row in csv_reader:
            url = row['url']
            current_price = findPrice(url)
            target_price = float(row['target'])
            if current_price is not None and current_price < target_price:
                sendEmail(row['name'],row['email'],current_price,target_price,url) #must include url also as a parameter
                print("Mail regarding price drop sent to ",row['email'])
                # schedule.cancel_job(check)




print("It is running")
schedule.every().day.at("17:10").do(check)

while True:
    schedule.run_pending()
    time.sleep(15)






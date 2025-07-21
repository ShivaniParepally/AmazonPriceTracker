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
    products =[]
    products_to_keep = []
    with open('storage.csv','r') as csvfile:
        csv_reader = list(csv.DictReader(csvfile))
        for row in csv_reader:
            products.append(row)
        
    for prod in products:
        url = prod['url']
        current_price = findPrice(url)
        target_price = float(prod['target'])
        print(current_price)
        if current_price is not None and current_price < target_price:
            sendEmail(prod['name'],prod['email'],current_price,target_price,url) #must include url also as a parameter
            print("Mail regarding price drop sent to ",prod['email'])
            # schedule.cancel_job(check)
        
        else:
            products_to_keep.append(prod)

    with open('storage.csv','w', newline='') as csvfile:
        fields= ['name','email','target','url']
        csv_writer= csv.DictWriter(csvfile,fieldnames=fields)
        csv_writer.writeheader()
        csv_writer.writerows(products_to_keep)




print("It is running")
schedule.every().day.at("14:43").do(check)

while True:
    schedule.run_pending()
    time.sleep(15)






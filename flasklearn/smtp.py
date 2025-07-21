import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from extract_price import findPrice
from dotenv import load_dotenv
import os

load_dotenv()

my_mailId = os.getenv("MY_EMAIL_ID")
password= os.getenv("EMAIL_PASSWORD")

# name= input("Enter recipient name: ")
# recipient_email = input("Enter recipient's mail id: ")

#url=input("Enter the url: ") #https://amzn.eu/d/eSv668i

#assuming these values for now

# dropped_price = findPrice()
# target_price=8000 # must get this value from the html frontend


def sendEmail(name,recipient_email,dropped_price,target_price,url):  # must include url also in this parameters list
    html_code= '''
    <html>
        <head></head>
        <body>
            <h1>Price Drop Alert!!</h1>
            <p>Dear {name},</p>
            <p><strong>Happy news!!</strong> We are thrilled to inform you that the price of the product you've been tracking has dropped to your specified target price!!<span>&#129395;&#129395;</span></p>
            <p>Your patience has paid off, and we're excited to help you seize this opportunity to make your purchase.</p>
            <p class="product">
                <b>Product name:</b><a href="{link}">View your product</a>
                <br>
                <b>Current Price:</b> {price}
                <br>
                <b>Your specified Target price: </b> {target}
            
            </p>

            <p>Now is the perfect time to make your purchse and enjoy this fantastic deal!. Simply click on the link above to go directly to the product page and complete your order.</p>
            <p>Happy shopping!!</p>

        </body>
    </html>
    '''.format(name=name,link=url, price=dropped_price,target=target_price) #must change link=url after getting url from frontend



    message = MIMEMultipart()
    message['From']= my_mailId
    message['To']= recipient_email
    message['Subject']= "Price Drop Alert!!"

    html_text= MIMEText(html_code,'html')
    message.attach(html_text)


    #def sendEmail():
        #if dropped_price < target_price:
            #with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connect:
                #connect.starttls()  #use this if you are only using smtplib.SMTP() for the connection (which is little insecure than smtplib.SMTP_SSL() )
                connect.login(user=my_mailId, password=password)
                #connect.sendmail(from_addr=my_mailId, to_addrs=recipient_email, msg="Subject:Price drop alert!!")
                connect.send_message(message)
        # else:
        #     print("Price didnt drop yet")


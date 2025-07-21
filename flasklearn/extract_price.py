import requests
import lxml
from bs4 import BeautifulSoup
import random
import logging

#url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
#url="https://amzn.eu/d/eSv668i"
#url = "https://amzn.in/d/3ssmlx3" # must get this url from the html frontend

#print(soup.prettify())


'''
price_element = soup.find(class_="a-offscreen")

if price_element:
    price = price_element.get_text()w
    price_without_currency = price.split("₹")[1]
    price_as_float = float(price_without_currency)
    print(price_as_float)
else:
    print("Price element not found")
'''

logging.basicConfig(level=logging.INFO)

def findPrice(url):
    # header = {
    # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    # "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    # }

    # "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36,gzip(gfe)"
    # "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"

    user_agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/93.0.961.52 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    ]

    user_agent = random.choice(user_agents)
    logging.info(f"{user_agent} is being used")

    response = requests.get(url, headers={"User-Agent":user_agent, "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"})

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        price = soup.find(class_="a-offscreen")

        if price:
            price = price.get_text()

            if "₹" in price:
                try:
                    price_without_currency = price.split("₹")[1]
                    price_without_commas = price_without_currency.replace(",","")
                    price_as_float = float(price_without_commas)
                    #print(price_as_float)
                    return price_as_float
                except IndexError as e:
                    logging.error(f"IndexError: {e} for price: {price}")
                except ValueError as e:
                    logging.error(f"ValueError: {e} for price : {price}")

            else:
                logging.error(f"₹ symbol is not found")
            
        else:
            logging.error(f"Cannot find price on page")

    else:
        logging.error("Failed to retrieve price. Status code: ",response.status_code)
    return None

# importing the libraries
from bs4 import BeautifulSoup
import requests
import smtplib
import time
from email.message import EmailMessage


def check_price():
    url=input("enter snapdeal product url")
    # Make a GET request to fetch the raw HTML content
    html_snapdeal = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_snapdeal, "lxml")

    price_sp=int(soup.find('span',class_='payBlkBig').text)

    #paytm
    url2=input("enter paytm url")
    html_paytm = requests.get(url2).text

    # Parse the html content
    soup = BeautifulSoup(html_paytm, "lxml")

    price_pt=int((soup.find('span',class_="_1V3w").text))


    url3=input("enter shopclues product url")
    # Make a GET request to fetch the raw HTML content
      
    # Make a GET request to fetch the raw HTML content
    html_shopclues = requests.get(url3).text
    rP=input("enter the price at which you want to send mail")
    requiredPrice=int(rP)
    # Parse the html content
    soup = BeautifulSoup(html_shopclues, "lxml")

    p=(soup.find('span',class_="f_price").get_text())
    pr=p.strip()
    price_sc=int(pr.strip('Rs.'))

    def minimum(): 
        list = [price_sp,price_pt,price_sc] 
        return min(list)
      
    minimumOfPrices=minimum()
    print("minimum price is {}".format(minimumOfPrices))
    

    if minimumOfPrices>requiredPrice:
       send_mail()

def send_mail():
        msg = EmailMessage()
        msg.set_content('Email sending example using Python. It\'s Simple Text Message')

        fromEmail = 'hollandislou@gmail.com'
        toEmail = 'monishasuthapalli688@gmail.com'

        msg['Subject'] = 'Simple Text Message'
        msg['From'] = fromEmail
        msg['To'] = toEmail

        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login('hollandislou@gmail.com', 'bhashyam')
        s.send_message(msg)
        s.quit()

while(True):
    check_price()
    time.sleep(60*60*60)
     




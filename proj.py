# importing the libraries
from bs4 import BeautifulSoup
import requests

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

# Parse the html content
soup = BeautifulSoup(html_shopclues, "lxml")

p=(soup.find('span',class_="f_price").get_text())
pr=p.strip()
price_sc=int(pr.strip('Rs.'))




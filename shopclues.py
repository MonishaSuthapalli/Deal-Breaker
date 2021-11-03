# importing the libraries
from bs4 import BeautifulSoup
import requests

url=input("enter shopclues product url")
# Make a GET request to fetch the raw HTML content
html_shopclues = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_shopclues, "lxml")

p=(soup.find('span',class_="f_price").get_text())
pr=price.strip()
price=p.strip('Rs.')
print(int(price))

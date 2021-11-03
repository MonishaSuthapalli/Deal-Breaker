# importing the libraries
from bs4 import BeautifulSoup
import requests

url=input("enter snapdeal product url")
# Make a GET request to fetch the raw HTML content
html_paytm = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_paytm, "lxml")

price=(soup.find('span',class_="_1V3w").text)
print(price)

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.amazon.com/CreepyParty-Novelty-Halloween-Costume-Party/dp/B0199PV50K/ref=pd_sim_21_3?_encoding=UTF8&pd_rd_i=B0199PV50K&pd_rd_r=9CN0FB2X3B4YRY4JBSHW&pd_rd_w=yoPuL&pd_rd_wg=AsYde&psc=1&refRID=9CN0FB2X3B4YRY4JBSHW')

soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())
price = soup.find('span', {'class' : 'a-size-medium a-color-price'})

print(price)

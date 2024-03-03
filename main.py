from bs4 import BeautifulSoup
import requests
import smtplib # For sending emails to yourself
import time
import datetime

# Connect to the website (Multiple website to automate a data collection thing to run periodically and update the price and/or avalilability of a product?)
url = 'https://store.nikon.ca/nikon-products/product/mirrorless-cameras/z-f.html'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
soup2 = soup.prettify()
title = soup2.find().get_text()
print (title)
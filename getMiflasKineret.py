import requests

from bs4 import BeautifulSoup
#
# get page
response = requests.get('http://kineret.org.il/miflasim/')
# let's soup the page
content = BeautifulSoup(response.content, 'html.parser')
# header
a=2
b=3
print("liran AMRANI")
print(a+b)
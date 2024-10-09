import requests
import time
from bs4 import BeautifulSoup

# first, let's make this work on a dummy static site.

webpage_response = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")

webpage = webpage_response.content
#print(webpage)
#ok, so it works
soup = BeautifulSoup(webpage, "html.parser")
print(soup)

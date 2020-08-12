import requests
from bs4 import BeautifulSoup

# Create variable that makes request to website
res = requests.get('https://news.ycombinator.com/news')

print(res)
import requests
from bs4 import BeautifulSoup
import pprint

# Create variable that makes request to website
res = requests.get('https://news.ycombinator.com/news')
# Requests from page 2 of website
res2 = requests.get('https://news.ycombinator.com/news?p=2')

# Convert the string into html
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser') # For page 2

# Use CSS Selectors to access title and score classes of website
links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')
# votes = soup.select('.score')

# Combine the two pages
mega_links = links + links2
mega_subtext = subtext + subtext2

# Sort articles in descending vote order
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

# Create function that takes links and votes as arguments
def create_custom_hn(links, subtext):
    hn = [] # Empty hackernews list
    # Loop through all the links and return the titles and hrefs (no html)
    for idx, item in enumerate(links):
        # .getText is BeautifulSoup's way of returning only text (not html)
        title = links[idx].getText()
        # None is the default in case the link is broken or unavailable
        href = links[idx].get('href', None)
        # Loop through the subtext class and get the child class score
        vote = subtext[idx].select('.score')
        # If vote has a number, get it
        if len(vote):
            # Get the scores as strings, remove word 'points' and convert to integers
            # points = int(votes[idx].getText().replace(' points', ''))
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                # print(points)
                # Send each article's title and link to the 'hn' list
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))


# print(votes[0])
# print(soup.select('.storylink')[0]) # Grab the class storylink for the first title
# print(soup.select('#score_24135032'))
# print(soup.select('.score'))
# print(soup.find(id='score_24135032'))
# print(soup.find_all('a'))
# print(soup.find_all('div'))
# print(soup.a)
# print(soup.find('a'))
# print(soup.title)
# print(soup.body.contents)
# print(soup.body)
# print(soup)
# print(res.text) 
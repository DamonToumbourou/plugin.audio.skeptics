import requests
import re
from bs4 import BeautifulSoup as bs

def get_soup(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')

    return soup

def get_podcast(url):
    # get html
    soup = get_soup(url)

    # parse html for useful links 
    content = soup.find('div', {'class': 'podcasts-detail'})
    content = content.find_all('li')
   
    output = []

    for i in content:
        try:
            label = i.find('a')
            label = i.get_text()
            label = re.search('Episode(.*)$', label).group(0)
            path = i.find_all('a')[1].get('href')
            
            img = i.find('img').get('src')

        except AttributeError:
            continue
        
        items = {
                'label': label,
                'path': path,
                'thumbnail': img,
        }

        output.append(items)

    return output
#get_podcast('http://www.theskepticsguide.org/podcast/sgu')

def get_podcast_content(url):
    soup = get_soup(url)
    content = soup.find('div', {'class': 'podcast-detail'})

    title = content.find('h1').get_text()

    specific_content = soup.find_all('div', {'class': 'podcast-segment'})

    news_items = []
    for i in specific_content:
        find_word = i.find('h3').get_text()

        if """What's the Word""" in find_word:
            word = i.find('span', {'class': 'podcast-item-value'}).get_text()
        
        if "News Items" in find_word:
            items = i.find_all('li')
            for k in items:
                label = k.find('span', {'class': 'podcast-item-label'}).get_text()
                value = k.find('span', {'class': 'podcast-item-value'}).get_text()
                print value
                

get_podcast_content('http://www.theskepticsguide.org/podcast/sgu/549')

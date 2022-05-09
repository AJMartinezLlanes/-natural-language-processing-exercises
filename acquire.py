from requests import get
from bs4 import BeautifulSoup
import pandas as pd


# codeup.com/blog scrapping functions
def parse_blog(blog):
    '''
    This function takes the information scraped from codeup blog page and return a dataframe with:
    title, date, tags and content of each blog 
    '''
    output = {}
    output['title'] = blog.find('h2').text
    output['date'] = blog.find('p').text[:12]
    output['tags'] = blog.find('p').text[14:]
    output['content'] = blog.find_all('p')[1].text
    return output

def scrape_codeup():
    '''
    This function will scrape 16 blogs from codeup blog page.
    '''
    headers = {'user-agent': 'Innis Data Science Cohort'}
    url = 'https://codeup.com/blog/'
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    blogs = soup.find_all('article')[:15]
    df = pd.DataFrame([parse_blog(blog) for blog in blogs])
    return df


# inshorts.com scraping functions
def parse_shorts(short):
     '''
    This function takes the information scraped from shorts page and return a dataframe with:
    title, date, tags and content of each article 
    '''
    output = {}
    output['title'] = short.find('span', itemprop= 'headline').text
    output['date'] = short.find('span', class_= 'date').text, short.find('span', class_= 'time').text
    output['author'] = short.find('span', class_= 'author').text
    output['content'] = short.find('div', itemprop= 'articleBody').text
    return output

def scrape_tech_shorts():
    '''
    This function will scrape technology articles from inshorts webpage
    '''
    url = 'https://inshorts.com/en/read/technology'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    shorts = soup.select('.news-card')
    df = pd.DataFrame([parse_shorts(short) for short in news])
    return df

def scrape_sports_shorts():
    '''
    This function will scrape sports articles from inshorts webpage
    '''
    url = 'https://inshorts.com/en/read/sports'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    shorts = soup.select('.news-card')
    df = pd.DataFrame([parse_shorts(short) for short in news])
    return df

def scrape_entertainment_shorts():
    '''
    This function will scrape entertainment articles from inshorts webpage
    '''
    url = 'https://inshorts.com/en/read/entertainment'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    shorts = soup.select('.news-card')
    df = pd.DataFrame([parse_shorts(short) for short in news])
    return df

def scrape_busines_shorts():
    '''
    This function will scrape business articles from inshorts webpage
    '''
    url = 'https://inshorts.com/en/read/business'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    shorts = soup.select('.news-card')
    df = pd.DataFrame([parse_shorts(short) for short in news])
    return df
import requests
from bs4 import BeautifulSoup
from finder import find
import re
import sys

def get_soup(URL):    
    reqs = requests.get(URL)
    soup = BeautifulSoup(reqs.text,'html.parser')
    return soup

def search_urls(soup):
    urls = find(soup, "a", "href");
    return urls

def search_images(soup):
    images = find(soup, "img", "src");
    return images

def search_emails(soup):
    content = find(soup, "p");

    emailRegex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)") 
    mo = emailRegex.search(content) 

    if not mo:
        content = "No email"
    return content

if __name__=="__main__":
    URL = sys.argv[1];
    soup = get_soup(URL);

    print("-" * 10, "URLS", "-" * 10)
    print(search_urls(soup));

    print("-" * 10, "IMAGES", "-" * 10)
    print(search_images(soup));

    print("-" * 10, "MAILS", "-" * 10)
    print(search_emails(soup));
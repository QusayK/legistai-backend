import requests
from bs4 import BeautifulSoup

def scrape_pdf_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = []
    for link in soup.find_all('a'):
        href = link.get('href')

        if href and href.endswith('.pdf'):
            links.append(href)
            
    return links
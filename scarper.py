import requests
from bs4 import BeautifulSoup

def scrape():
    url = 'https://www.sfu.ca/students/calendar/2024/fall/courses/cmpt.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)



if __name__ == '__main__':
    scrape()
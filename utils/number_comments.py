import requests
from bs4 import BeautifulSoup


def get_number_comments(postid: int = 14):
    url = f'http://127.0.0.1:5000/blog/{postid}'
    res = requests.get(url)
    html_page = res.text

    soup = BeautifulSoup(html_page, 'html.parser')
    soup.prettify()

    number_comments = soup.findAll("span")
    print(number_comments)
    return number_comments

get_number_comments(14)
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def index(request):
    response = requests.get('https://www.dawn.com/must-read')
    soup = BeautifulSoup(response.text, 'html.parser')

    news = []

    stories = soup.select('.box.story')
    for story in stories:
        img = story.find('img')
        url = story.find('a')
        title = story.select_one('.story__link').getText()
        excerpt = story.select_one('.story__excerpt').getText()
        published_at = story.select_one('.timestamp--time').getText()

        context = {
            'img': img['src'],
            'title': title,
            'excerpt': excerpt,
            'published_at': published_at,
            'url': url['href'],
        }
        news.append(context)
    

    return render(request, 'index.html', { 'news': news })
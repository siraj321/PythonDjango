import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests import Session
from requests.compat import quote_plus
from . import models

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/bbb?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search =  request.POST.get('search')
    models.Search.objects.create(search = search) # create entry in database
    #print(quote_plus(search))
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))



    s = requests.Session()
    #response = requests.get('https://losangeles.craigslist.org/search/bbb?query=python%20tutor',verify=False)
    response = requests.get(final_url, verify=False)
    print('final_url:',final_url)
    #request = requests.Request('GET', 'https://losangeles.craigslist.org/search/bbb?query=python%20tutor',verify=False)
    #prepared_request = s.prepare_request(request)
    #settings = s.merge_environment_settings(prepared_request.url, None, None, None, None)
    #response = s.send(prepared_request, **settings)
    #response = s.send(prepared_request)...
    data = response.text
    soup = BeautifulSoup(data,features='html.parser')

    post_listings = soup.find_all('li',{'class':'result-row'})
    post_title = post_listings[0].find(class_='result-title').text
    post_url = post_listings[0].find('a').get('href')
    post_price = post_listings[0].find(class_='result-price')

    final_postings = []

    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price')
        else: post_price = 'N/A'

        final_postings.append((post_title, post_url, post_price))


    #post_text = new_soup.find(id='postingbody').text
    #print(post_title)
    #print(post_url)
    #print(post_price)

    #post_titles = soup.find_all('a',{'class':'result-title'})
    #print('post_titles:',post_title[0].text)
    #print('post_titles:', post_title[0].get('href'))
    #print(data)
    stuff_for_frontend = {
        'search':search,
        'final_postings': final_postings,

    }
    return render(request, 'my_app/new_search.html',stuff_for_frontend)


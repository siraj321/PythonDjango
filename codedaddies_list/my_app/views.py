import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests import Session
from requests.compat import quote_plus
from . import models

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search =  request.POST.get('search')


    s = requests.Session()
    response = requests.get('https://losangeles.craigslist.org/search/bbb?query=python%20tutor',verify=False)
    #request = requests.Request('GET', 'https://losangeles.craigslist.org/search/bbb?query=python%20tutor',verify=False)
    #prepared_request = s.prepare_request(request)
    #settings = s.merge_environment_settings(prepared_request.url, None, None, None, None)
    #response = s.send(prepared_request, **settings)
    #response = s.send(prepared_request)...

    data = response.text
    print(data)
    stuff_for_frontend = {
        'search':search,
    }
    return render(request, 'my_app/new_search.html',stuff_for_frontend)


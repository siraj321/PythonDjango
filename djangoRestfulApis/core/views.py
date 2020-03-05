from django.shortcuts import render
from django.conf import settings
import requests
from github import Github, GithubException
from .forms import DictionaryForm

def home(request):
    is_cached = ('geodata' in request.session)

    if not is_cached:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
        #response = requests.get('http://api.ipstack.com/%s' % ip_address, verify=False)
        params = {'access_key': settings.IPSTACK_API_KEY}
        response = requests.get('http://api.ipstack.com/14.143.89.237', params=params, verify=False)
        #response = requests.get('http://freegeoip.net/json/10.0.2.124', verify=False)
        #params = {'access_key': settings.IPSTACK_API_KEY}
        print(ip_address)
        #response = requests.get('http://api.ipstack.com/%s' % ip_address, params=params,verify=False)
        #response = requests.get('http://api.ipstack.com/%s' % ip_address, params=params, verify=False)
        request.session['geodata'] = response.json()

    geodata = request.session['geodata']

    return render(request, 'core/home.html', {
        'ip': geodata.get('14.143.89.237'),
        'country': geodata.get('country_name', 'India'),
        'latitude': geodata.get('latitude', '22.307159'),
        'longitude': geodata.get('longitude', '73.181221'),
        'api_key': 'AIzaSyCdp2_-FjODIAz10WlSD839WsL7fF0NMEs',
        #'api_key': settings.GOOGLE_MAPS_API_KEY,
        'is_cached': is_cached
    })


def github(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url,verify=False)
        search_was_successful = (response.status_code == 200)  # 200 = SUCCESS
        search_result = response.json()
        search_result['success'] = search_was_successful
        search_result['rate'] = {
            'limit': response.headers['X-RateLimit-Limit'],
            'remaining': response.headers['X-RateLimit-Remaining'],
        }
    return render(request, 'core/github.html', {'search_result': search_result})


def github_client(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        client = Github()

        try:
            user = client.get_user(username)
            search_result['name'] = user.name
            search_result['login'] = user.login
            search_result['public_repos'] = user.public_repos
            search_result['success'] = True
        except GithubException as ge:
            search_result['message'] = ge.data['message']
            search_result['success'] = False

        rate_limit = client.get_rate_limit()
        search_result['rate'] = {
            'limit': rate_limit.rate.limit,
            'remaining': rate_limit.rate.remaining,
        }

    return render(request, 'core/github.html', {'search_result': search_result})


def oxford(request):
    search_result = {}
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = DictionaryForm()
    return render(request, 'core/oxford.html', {'form': form, 'search_result': search_result})

from django.shortcuts import render
import requests

def home(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()

    print(response)

    return render(request, 'core/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })
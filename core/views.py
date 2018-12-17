from django.shortcuts import render
import requests

def home(request):
    response = requests.get('http://ddragon.leagueoflegends.com/cdn/8.13.1/data/en_US/champion.json')
    geodata = response.json()
    #print(geodata.keys())
    return render(request, 'core/home.html', {
        'type': geodata['type'],
        'format': geodata['format'],
        'version': geodata['version'],
        'data': geodata['data'],
    })

def first(request):
    response = requests.get('http://ddragon.leagueoflegends.com/cdn/8.13.1/data/en_US/champion.json')
    geodata = response.json()
    #print(geodata.keys())
    return render(request, 'core/first.html', {
        'type': geodata['type'],
        'format': geodata['format'],
        'version': geodata['version'],
        'data': geodata['data'],
    })

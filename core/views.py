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

    is_cached = ('champdata' in request.session)

    if not is_cached:
	    response = requests.get('http://ddragon.leagueoflegends.com/cdn/8.13.1/data/en_US/champion.json')
	    request.session['champdata'] = response.json()

    champdata = request.session['champdata']


    return render(request, 'core/first.html', {
        'type': champdata['type'],
        'format': champdata['format'],
        'version': champdata['version'],
        'data': champdata['data'],

        'is_cached': is_cached,
        # add detail data
        'champion_name': list(champdata['data'].keys()),

    })

def second(request):

    is_cached = ('champdata' in request.session)

    if not is_cached:
        response = requests.get('http://ddragon.leagueoflegends.com/cdn/8.13.1/data/en_US/champion.json')
        request.session['champdata'] = response.json()

    champdata = request.session['champdata']
    #print(champdata.keys())

    #search
    if request.method == 'GET':
        print('it was get')

        role_query = request.GET.getlist('roles', None)
        #search_query = request.GET.get('search_box', None)

        if role_query:
            #print(type(role_query))
            print(role_query)
        else:
            print('there was nothing')








    return render(request, 'core/second.html', {
        'type': champdata['type'],
        'format': champdata['format'],
        'version': champdata['version'],
        'data': champdata['data'],

        'is_cached': is_cached,
        # add detail data
        'champion_name': list(champdata['data'].keys()),

    })
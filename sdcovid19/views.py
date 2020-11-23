from django.shortcuts import render
import requests
import datetime

def home(request):
    response  = requests.get('https://covid19.sd/data.json')
    covidata  = response.json()
    now = datetime.datetime.now()
    context   = {
                    'cases'     : covidata['cases'],
                    'tdCases'   : covidata['todayCases'],
                    'deaths'    : covidata['deaths'],
                    'tdDeaths'  : covidata['todayDeaths'],
                    'recovered' : covidata['recovered'],
                    'actCases'  : covidata['activeCases'],
                    'critical'  : covidata['critical'],
                    'now': now
                }

    return render(request, 'index.html', context)

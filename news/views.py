from django.shortcuts import render,HttpResponseRedirect
from .forms import RegistrationForm
import requests

# Create your views here.


basrUrl = "https://api.covid19api.com/"


def covid19_country(request):
    # if 'country' in request.GET:
    # country = request.GET['country']
    url = "{}countries".format(basrUrl)
    response = requests.get(url)
    text = response.json()
    return render(request, 'index.html', {'country_info': text})


def index(request):
    return render(request, 'html/index.html')


def contact_us(request):
    return render(request, 'html/contact.html')


def countries(request):
    return render(request, 'html/countries.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register/')
    else:
            form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})








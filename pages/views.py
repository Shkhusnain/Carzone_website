from django.shortcuts import render
from .models import Team
from cars.models import Car

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('created_date').filter(is_featured = True)
    all_cars = Car.objects.order_by('created_date')
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    style_search = Car.objects.values_list('body_style',flat=True).distinct()
    model_search  = Car.objects.values_list('model',flat=True).distinct()
    transmission_search  = Car.objects.values_list('transmission',flat=True).distinct()
    data = {
        'teams': teams ,
        'featured_cars' : featured_cars,
        'all_cars' : all_cars,
        'city_search' : city_search,
        'model_search' : model_search,
        'year_search' : year_search,
        'style_search': style_search,
        'transmission_search ': transmission_search,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    teams = Team.objects.all()
    data = {
        'teams': teams ,
    }
    return render(request, 'pages/services.html', data)
    
def contact(request):
    return render(request, 'pages/contact.html')
    
def cars(request):
    return render(request, 'cars/cars.html')

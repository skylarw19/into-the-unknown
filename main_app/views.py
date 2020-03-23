from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Place

# class Place:  
#   def __init__(self, name, country, state, city, description):
#     self.name = name
#     self.country = country
#     self.state = state
#     self.city = city
#     self.description = description


# places = [
#     Place('Six Flags', 'USA', 'Texas', 'San Antonio', 'Six Flags Fiesta'),
#     Place('Sea World', 'USA', 'Texas', 'San Antonio', 'Shamu'),
#     Place('Schlitterbahn', 'USA', 'Texas', 'New Braunfels', 'Tubing in the lake'),
# ]

# Create your views here.

class PlaceCreate(CreateView):
    model = Place
    fields = '__all__'

class PlaceUpdate(UpdateView):
    model = Place
    fields = ['country', 'state', 'city', 'description']

class PlaceDelete(DeleteView):
    model = Place
    success_url = '/places/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def places_index(request):
    places = Place.objects.all()
    return render(request, 'places/index.html', {'places': places})

def places_detail(request, place_id):
    # place = Place.objects.get(id=place_id)
    place = places[place_id]
    return render(request, 'places/detail.html', {'place': place})


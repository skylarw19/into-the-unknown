from django.shortcuts import render
from .models import Place

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def places_index(request):
    # places = Place.objects.all()
    return render(request, 'places/index.html', {'places': places})

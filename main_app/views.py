from django.shortcuts import render

class Place:  
  def __init__(self, name, country, state, city, description):
    self.name = name
    self.country = country
    self.state = state
    self.city = city
    self.description = description


places = [
    Place('Six Flags', 'USA', 'Texas', 'San Antonio', 'Six Flags Fiesta'),
    Place('Sea World', 'USA', 'Texas', 'San Antonio', 'Shamu'),
    Place('Schlitterbahn', 'USA', 'Texas', 'New Braunfels', 'Tubing in the lake'),
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

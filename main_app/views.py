from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Place
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReviewForm

class PlaceCreate(LoginRequiredMixin,CreateView):
    model = Place
    fields = ['name', 'country', 'state', 'city', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlaceUpdate(LoginRequiredMixin, UpdateView):
    model = Place
    fields = ['country', 'state', 'city', 'description']

class PlaceDelete(LoginRequiredMixin, DeleteView):
    model = Place
    success_url = '/places/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def places_index(request):
    places = Place.objects.filter(user=request.user)
    return render(request, 'places/index.html', {'places': places})

@login_required
def places_detail(request, place_id):
    place = Place.objects.get(id=place_id)
    review_form = ReviewForm()
    return render(request, 'places/detail.html', {
        'place': place,
        'review_form': review_form
        })

@login_required
def add_review(request, place_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.place_id = place_id
        new_review.save()
    return redirect('places_detail', place_id=place_id)
    
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
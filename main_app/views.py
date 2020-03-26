from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Place, Review, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReviewForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'intotheunknown'


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

@login_required 
def delete_review(request, place_id, review_id):
    Review.objects.get(id=review_id).delete()
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

def add_photo(request, place_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, place_id=place_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('places_detail', place_id=place_id)
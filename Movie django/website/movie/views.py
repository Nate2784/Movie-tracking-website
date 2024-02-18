from django.shortcuts import render, HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.
# images
icon = image.objects.get(name='icon')
about = image.objects.get(name='about')
service = image.objects.get(name='service')
addlist = image.objects.get(name='addlist')
purchase = image.objects.get(name='onlinePurchase')
ticket = image.objects.get(name='ticket')
# end of images
info = ComapanyInformation.objects.first()
images = image.objects.all()
trending = Trending_movie.objects.all()
movies = movie.objects.all()
shows = show.objects.all()
cinema = cinema_item.objects.all()
# genres
action = get_object_or_404(Genre, name='Action')
family = get_object_or_404(Genre, name='Family')
animation = get_object_or_404(Genre, name='Animation')
comedy = get_object_or_404(Genre, name='Comedy')
action_movies = movie.objects.filter(genre = action)
comedy_movies = movie.objects.filter(genre = comedy)
animation_movies = movie.objects.filter(genre = animation)
action_series = show.objects.filter(genre = action)
family_series = show.objects.filter(genre = family)


data ={
    'icon':icon,
    'ticket':ticket,
    'about':about,
    'service':service,
    'addlist':addlist,
    'purchase':purchase,
    'info':info,
    'images':images,
    'info':info,
    'trending':trending,
    'movies':movies,
    'shows':shows,
    'cinema':cinema,
    'action':action_movies,
    'animation':animation_movies,
    'comedy':comedy_movies,
    'action_series':action_series,
    'family_series':family_series
}
def home(request):
    return render(request, 'index.html', data)

def movies(request):
    return render(request, 'movies.html', data)

def tv_shows(request):
    return render(request, 'tv_shows.html',data)

def incinema(request):
    return render(request, 'in_cinema.html',data)

def wachlist(request):
    return render(request, 'watchlist.html',data)

def about(request):
    return render(request, 'about.html',data)

def contact(request):
    return render(request, 'contact.html',data)

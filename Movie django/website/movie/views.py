from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here

def home(request):
        
    icon = image.objects.get(name='icon')
    info = ComapanyInformation.objects.first()
    trending = Trending_movie.objects.all()
    movies = movie.objects.all()
    shows = show.objects.all()
    
    data ={
    'icon':icon,
    'info':info,
    'trending':trending,
    'movies':movies,
    'shows':shows,
    }
    return render(request, 'index.html', data)

def movies(request):
        
    icon = image.objects.get(name='icon')
    info = ComapanyInformation.objects.first()
    movies = movie.objects.all()
    data ={
    'icon':icon,
    'info':info,
    'movies':movies,
    }
    return render(request, 'movies.html', data)

def tv_shows(request):
    
    icon = image.objects.get(name='icon')
    info = ComapanyInformation.objects.first()
    shows = show.objects.all()
    data ={
    'icon':icon,
    'info':info,
    'shows':shows,
    }
    return render(request, 'tv_shows.html',data)

def incinema(request):
    
    icon = image.objects.get(name='icon')
    info = ComapanyInformation.objects.first()
    cinema = cinema_item.objects.all()
    ticket = image.objects.get(name='ticket')
    data ={
    'icon':icon,
    'ticket':ticket,
    'info':info,
    'cinema':cinema,
    }
    return render(request, 'in_cinema.html',data)

def wachlist(request):
    
    icon = image.objects.get(name='icon')
    info = ComapanyInformation.objects.first()
    trending = Trending_movie.objects.all()
    movies = movie.objects.all()
    shows = show.objects.all()

    data ={
    'icon':icon,
    'info':info,
    'trending':trending,
    'movies':movies,
    'shows':shows,
    }
    return render(request, 'watchlist.html',data)

def about(request):
        
    icon = image.objects.get(name='icon')
    info = ComapanyInformation.objects.first()
    about = image.objects.get(name='about')
    service = image.objects.get(name='service')
    addlist = image.objects.get(name='addlist')
    purchase = image.objects.get(name='onlinePurchase')
    
    data ={
    'icon':icon,
    'about':about,
    'service':service,
    'addlist':addlist,
    'purchase':purchase,
    'info':info,
    }
    return render(request, 'about.html',data)


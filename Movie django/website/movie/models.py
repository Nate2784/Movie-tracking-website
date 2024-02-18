from django.db import models

# Create your models here.

class image(models.Model):
   name  = models.CharField(max_length=100)
   image  = models.ImageField(null=True)
   
   def __str__(self) -> str:
      return self.name
   
class ComapanyInformation(models.Model):
   name  = models.CharField(max_length=100)
   about = models.TextField()
   service = models.TextField()
   addLIst = models.TextField()
   onlinePurchase = models.TextField()
   
   def __str__(self) -> str:
      return self.name
   
class Genre(models.Model):
   name  = models.CharField(max_length=100)
   

   def __str__(self) -> str:
      return self.name
   
   
class movie(models.Model):
   movie_name = models.CharField(max_length=100)
   movie_description = models.TextField()   
   genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
   image  = models.ImageField(null=True)
   year   = models.CharField(max_length=100)
   
   def __str__(self) -> str:
      return self.movie_name
   
class show(models.Model):
   show_name = models.CharField(max_length=100)
   show_description = models.TextField()   
   genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
   image  = models.ImageField(null=True)
   year   = models.CharField(max_length=100)
   
   def __str__(self) -> str:
      return self.show_name
   
class Trending_movie(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField()
   image  = models.ImageField(null=True)
   
   def __str__(self) -> str:
      return self.name

class cinema_item(models.Model):
   TIME_CHOICES = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
    ]
   movie_name = models.CharField(max_length=100)
   movie_description = models.TextField()  
   image  = models.ImageField(null=True)
   show_time = models.CharField(max_length=100, choices=TIME_CHOICES)
   duraion = models.CharField(max_length=100, null=True)
   open_seats =models.IntegerField()
   
   def __str__(self) -> str:
      return self.movie_name
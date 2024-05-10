import sys
import os
import django
from django.db import models

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()



class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    release_year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title






# Створюємо декілька жанрів
genre1 = Genre.objects.create(name="Action")
genre2 = Genre.objects.create(name="Adventure")
genre3 = Genre.objects.create(name="RPG")

# Створюємо декілька ігор
game1 = Game.objects.create(title="The Witcher 3: Wild Hunt", release_year=2015, rating=9.3)
game1.genres.add(genre1, genre3)  # Додаємо жанри до гри

game2 = Game.objects.create(title="Uncharted 4: A Thief's End", release_year=2016, rating=9.5)
game2.genres.add(genre1, genre2)

game3 = Game.objects.create(title="Red Dead Redemption 2", release_year=2018, rating=9.8)
game3.genres.add(genre1, genre2)

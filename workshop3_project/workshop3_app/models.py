from django.db import models


class Movie(models.Model):
    name = models.TextField()
    year = models.TextField()
    genre = models.TextField()


class Attend(models.Model):
    ATTN_Number = models.IntegerField()
    Movie_Name = models.TextField()
    seat_number = models.TextField()
    show_time = models.TextField()

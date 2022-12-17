from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from datetime import datetime


class Artist(models.Model):
    first_name = models.CharField('First Name', max_length=60, blank=False, null=False)
    last_name = models.CharField('Last Name', max_length=60, blank=False, null=False)
    birth_date = models.CharField('Birth Date', max_length=10, blank=True, null=True)
    photo = models.ImageField('Photo', blank=True, null=True)
    bio = models.CharField('Bio', max_length=360, blank=False, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Play(models.Model):
    title = models.CharField('Title', max_length=60, unique=True, blank=False, null=False)
    genre = models.CharField('Genre', max_length=20, blank=False, null=False)
    date = models.DateField('Date', blank=False, null=False)
    time = models.TimeField('Time', blank=False, null=False)
    description = models.CharField('Description', max_length=360, blank=True, null=True)
    artists = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True)
    price = models.CharField('Price', max_length=10, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Play, self).save(*args, **kwargs)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('play-details', kwargs={"slug": self.slug})


class Ticket(models.Model):
    seat_number = models.IntegerField('Seat Number', unique=True)
    price = models.DecimalField('Price', max_digits=5, decimal_places=2)
    play = models.ForeignKey(Play, on_delete=models.CASCADE)

    def __str__(self):
        return f"Play {self.play} - Seat: {self.seat_number} - Date: {self.play.date} - Time: {self.play.time}"


class User(models.Model):
    username = models.CharField('username', max_length=30, blank=False, null=False)
    password = models.CharField('password', max_length=30, blank=False, null=False)
    email = models.EmailField('E-mail', blank=False, null=False)
    first_name = models.CharField('First Name', max_length=60, blank=False, null=False)
    last_name = models.CharField('Last Name', max_length=60, blank=False, null=False)
    tickets = models.ManyToManyField(Ticket)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class News(models.Model):
    title = models.CharField('Title', max_length=60, unique=True, blank=False, null=False)
    date = models.DateField('Date', blank=False, null=False, default=datetime.now)
    time = models.TimeField('Time', blank=False, null=False, default=datetime.now)
    content = models.CharField('Content', max_length=360, blank=True, null=True)

    class Meta:
        ordering = ['date']

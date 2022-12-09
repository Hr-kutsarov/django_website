from django.db import models


class Artist(models.Model):
    first_name = models.CharField('First Name', max_length=60, blank=False, null=False)
    last_name = models.CharField('Last Name', max_length=60, blank=False, null=False)
    photo = models.ImageField('Photo')
    bio = models.CharField('Bio', max_length=360, blank=False, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Play(models.Model):
    title = models.CharField('Title', max_length=60, blank=False, null=False)
    genre = models.CharField('Genre', max_length=20, blank=False, null=False)
    date = models.DateField('Date', blank=False, null=False)
    time = models.TimeField('Time', blank=False, null=False)
    description = models.CharField('Description', max_length=360, blank=True, null=True)
    artists = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Ticket(models.Model):
    seat_number = models.IntegerField('Seat Number')
    price = models.DecimalField('Price', max_digits=5, decimal_places=2)
    play = models.ForeignKey(Play, on_delete=models.CASCADE)


class User(models.Model):
    username = models.CharField('username', max_length=30, blank=False, null=False)
    password = models.CharField('password', max_length=30, blank=False, null=False)
    email = models.EmailField('E-mail', blank=False, null=False)
    first_name = models.CharField('First Name', max_length=60, blank=False, null=False)
    last_name = models.CharField('Last Name', max_length=60, blank=False, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



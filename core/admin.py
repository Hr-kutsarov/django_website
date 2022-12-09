from django.contrib import admin
from .models import Artist, Play, Ticket, User

admin.site.register(Artist)
admin.site.register(Play)
admin.site.register(Ticket)
admin.site.register(User)

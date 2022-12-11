from django.contrib import admin
from .models import Artist, Play, Ticket, User

admin.site.register(Artist)

admin.site.register(Ticket)
admin.site.register(User)


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

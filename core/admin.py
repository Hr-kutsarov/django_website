from django.contrib import admin
from .models import Artist, Play, News

admin.site.register(Artist)


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

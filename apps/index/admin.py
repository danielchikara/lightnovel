from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(RolUser)
admin.site.register(UserNovel)
admin.site.register(ReadingList)
admin.site.register(Genre)
admin.site.register(SubGenre)
admin.site.register(Novel)
admin.site.register(Chapter)
    
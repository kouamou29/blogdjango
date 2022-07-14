from django.contrib import admin

# Register your models here.
from src.models import Comments, Post

admin.site.register(Post)
admin.site.register(Comments)
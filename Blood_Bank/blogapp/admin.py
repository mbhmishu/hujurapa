from django.contrib import admin
from blogapp.models import Blog, Comment,Likes,Follow

# Register your models here.
admin.site.register(Blog)
admin.site.register(Likes)
admin.site.register(Follow)

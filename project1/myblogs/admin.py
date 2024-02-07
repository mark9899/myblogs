from django.contrib import admin
from .models import  Blog_Category,blog_Post


# Register your models here.
admin.site.register(Blog_Category)
admin.site.register(blog_Post)


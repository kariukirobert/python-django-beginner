from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'slug', 'content')


admin.site.register(BlogPost, BlogPostAdmin)


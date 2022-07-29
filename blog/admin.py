from django.contrib import admin
from .models import Post
from django.db import models
# Register your models here.

from tinymce.widgets import TinyMCE




class PostAdmin(admin.ModelAdmin):
    
    list_display = ['title','update','created','status' ]
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title', 'content']
    list_filter = ['update', 'status']


admin.site.register(Post, PostAdmin)
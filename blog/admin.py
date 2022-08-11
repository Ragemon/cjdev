from django.contrib import admin
from .models import Post, PostContent
from django.db import models
# Register your models here.

from tinymce.widgets import TinyMCE


class PostContentInline(admin.StackedInline):
    model = PostContent
    field = '__all__'
    # extra = 0
    # formfield_overrides = {
    #     models.TextField: {
    #         'widget': TinyMCE
    #     }
    # }
    
class PostAdmin(admin.ModelAdmin):
    inlines = [ PostContentInline ]
    
    list_display = ['title','update','created','status', 'category', ]
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title', 'content']
    list_filter = ['update', 'status', 'category']
    formfield_overrides = {
        models.TextField: {
            'widget': TinyMCE
        }
    }





admin.site.register(Post, PostAdmin)
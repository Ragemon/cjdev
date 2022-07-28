from django.contrib import admin
from .models import Post, BlogPost
from django.db import models
# Register your models here.

from tinymce.widgets import TinyMCE


# Apply summernote to all TextField in model.
# class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
#     summernote_fields = '__all__'
#
#
# admin.site.register(SomeModel, SomeModelAdmin)

class PostAdmin(admin.ModelAdmin):
    # summernote_fields = '__all__'
    list_display = ['title','update','created','status' ]
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title', 'content']
    list_filter = ['update', 'status']

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['header']
    formfield_overrides = { models.TextField: {'widget': TinyMCE()}
}

#admin.site.register(BlogPost, BlogPostAdmin)

admin.site.register(Post, PostAdmin)
from django.contrib import admin
from .models import Post
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin



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


admin.site.register(Post, PostAdmin)
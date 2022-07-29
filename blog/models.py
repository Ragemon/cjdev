import sqlite3
from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from tinymce import models as tinymce_models



# Create your models here.
from django.urls import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
        ('sketch', 'Sketch'),
    )
    CATEGORY_CHOICES = (
        ('blog','Blog'),
        ('song','Song'),
        ('other', 'Other'),
    )
    title = models.CharField(max_length=120)
    
    author = models.CharField(default='Courage', max_length=150)
    created = models.DateTimeField(auto_now=False,
                                     auto_now_add=True,
                                   null=True)

    update = models.DateTimeField(auto_now=True,
                                  auto_now_add=False)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="blog")
    slug = models.SlugField(max_length=1100, unique_for_date='created')

    comments = models.BooleanField(default=True)
##install Pillow from pip install Pillow to use image
    post_image = models.ImageField(upload_to='postimages',blank=True)
    tags = TaggableManager()
    content = tinymce_models.HTMLField()
    subcontent = models.TextField(blank=True, max_length=450)
    
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #         'blog:article-list',
    #
    #     )

    class meta:
        ordering = ['id']

    





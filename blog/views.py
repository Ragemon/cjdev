from unicodedata import category
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import (
            CreateView,
            DeleteView,
            ListView,
            DetailView
)
# Create your views here.


def post_create(request):
    template = ('blog/home.html')
    return render(request, template)

class ArticleDetailView(DetailView):
    queryset = Post.objects.filter(status='published')
    template_name = ('blog/post_detail.html')


class ArticleListView(ListView):
    model = Post
    queryset = Post.objects.filter(
        status='published', category='blog').order_by('-update')

    template_name = ('blog/post_list.html')
    paginate_by = 4





def post_update(request):
    template = ('blog/home.html')
    return render(request, template)

def post_delete(request):
    template = ('blog/home.html')
    return render(request, template)


def about(request):
    template = ('blog/about.html')
    return render(request, template)


def privacy_policy(request):
    template = ('blog/privacy_policy.html')
    return render(request, template)



def license(request):
    template = ('blog/comments.html')
    return render(request, template)
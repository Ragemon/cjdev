from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
        path('blog/snippet', views.SnippetListView.as_view(), name='snippet_list'),
        path('blog/snippet/', views.SnippetListView.as_view(), name='snippet_list'),
        path('en/snippet/<int:pk>/<slug:slug>', views.SnippetDetailView.as_view(), name='snippet_detail'),
        path('en/snippet/<int:pk>/<slug:slug>/', views.SnippetDetailView.as_view(), name='snippet_detail'),
        path('', views.ArticleListView.as_view(), name='article_list'),
        path('/', views.ArticleListView.as_view(), name='article_list'),
        path('en/edublog/<int:pk>/<slug:slug>', views.ArticleDetailView.as_view(), name='article_detail'),
        path('en/edublog/<int:pk>/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
        
        path('', views.post_update, name='update'),
        path('', views.post_delete, name='delete'),
        path('', views.post_delete, name='detail'),

        path('about', views.about, name='about'),
        path('privacy_policy', views.privacy_policy, name='privacy_policy'),
        path('license', views.license, name='license'),

]
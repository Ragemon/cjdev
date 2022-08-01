from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
        path('', views.ArticleListView.as_view(), name='article_list'),
        path('en/<int:pk>/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
        path('', views.post_update, name='update'),
        path('', views.post_delete, name='delete'),
        path('', views.post_delete, name='detail'),

        path('about/', views.about, name='about'),
        path('privacy_policy', views.privacy_policy, name='privacy_policy'),
        path('license', views.license, name='license'),

]
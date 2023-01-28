from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views


from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView



urlpatterns = []
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += path("__reload__/", include("django_browser_reload.urls"))



urlpatterns += [
    path('django-admin/', admin.site.urls),
    path('', include('blog.urls')),

    path('about/', blog_views.about, name='about'),
    path('privacy_policy/', blog_views.privacy_policy, name='privacy_policy'),
    path('license/', blog_views.license, name='license'),
    # path('blog/', include('blog.urls')),
    path('tinymce/', include('tinymce.urls')),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", 
            content_type="text/plain")),  #add the robots.txt file
   # automatic browser reloader
   path("ads.txt",TemplateView.as_view(template_name="ads.txt", 
            content_type="text/plain")),
    
    

]


print("urls start")
urlpatterns += staticfiles_urlpatterns()

print("urls end")

    # test_func in summernote upload view. (Allow upload images only when user passes the test)
    # https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
    
    
def example_test_func(request):
        return request.user.groups.filter(name='group_name').exists()
    
    



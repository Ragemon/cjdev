from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = []
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += path("__reload__/", include("django_browser_reload.urls"))



urlpatterns += [
    path('django-admin/', admin.site.urls),
    path('', include('blog.urls')),

    # path('blog/', include('blog.urls')),
    path('tinymce/', include('tinymce.urls')),
    
    # automatic browser reloader
    
    

]



urlpatterns += staticfiles_urlpatterns()



    # test_func in summernote upload view. (Allow upload images only when user passes the test)
    # https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
    
    
def example_test_func(request):
        return request.user.groups.filter(name='group_name').exists()
    
    



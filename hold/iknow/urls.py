from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('blog.urls')),

    # path('blog/', include('blog.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('summernote/', include('django_summernote.urls')),
    # automatic browser reloader
    path("__reload__/", include("django_browser_reload.urls")),
    

]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()



    # test_func in summernote upload view. (Allow upload images only when user passes the test)
    # https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
    
    
def example_test_func(request):
        return request.user.groups.filter(name='group_name').exists()
    
    



SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    'iframe': True,

    # Or, you can set it to `False` to use SummernoteInplaceWidget by default - no iframe mode
    # In this case, you have to load Bootstrap/jQuery sources and dependencies manually.
    # Use this when you're already using Bootstrap/jQuery based themes.
    # 'iframe': False,
    'test_func_upload_view': example_test_func,
    # You can put custom Summernote settings
    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,

        # Change editor size
        'width': '100%',
        'height': '480',

        # Use proper language setting automatically (default)
        'lang': None,

        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],

        # Or, explicitly set language/locale for editor
        'lang': 'ko-KR',


        # You can also add custom settings for external plugins
        'print': {
            'stylesheetUrl': '/some_static_folder/printable.css',
        },
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            # You have to include theme file in 'css' or 'css_for_inplace' before using it.
            'theme': 'monokai',
        },
    },

    # Require users to be authenticated for uploading attachments.
    'attachment_require_authentication': True,



    # Set custom storage class for attachments.
    'attachment_storage_class': 'my.custom.storage.class.name',

    # Set custom model for attachments (default: 'django_summernote.Attachment')
    'attachment_model': 'my.custom.attachment.model', # must inherit 'django_summernote.AbstractAttachment'

    # You can completely disable the attachment feature.
    'disable_attachment': False,

    # Set to `True` to return attachment paths in absolute URIs.
    'attachment_absolute_uri': False,


    

  

    # Codemirror as codeview
    # If any codemirror settings are defined, it will include codemirror files automatically.
    'css': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/theme/monokai.min.css',
    ),
}

    
SUMMERNOTE_THEME = 'bs4'
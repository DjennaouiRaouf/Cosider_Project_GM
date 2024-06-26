from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf import settings

from django.views.static import serve


urlpatterns = [


    path('admin/', admin.site.urls),
    path('sm/',include('api_sm.urls')),
    path('sch/', include('api_sch.urls')),
    path('forms/',include('forms.urls')),
    path('images/', include('images.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),


]

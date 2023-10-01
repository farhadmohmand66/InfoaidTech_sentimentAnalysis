from django.contrib import admin
from django.urls import path
from django.views.static import serve

from django.conf.urls import include
from django.urls import re_path
urlpatterns = [
    re_path('', include('saApp.urls')),
    path('admin/', admin.site.urls),
]
"""calc2 URL Configuration

"""
from django.contrib import admin
from django.urls import path
from calculator import views
from django.urls import path, include
from django.conf import settings
from django.urls.conf import include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index', views.index),
    path('create',views.getdata),
]

"""wallpaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from wallpaper.views import *

urlpatterns = [
    path('bing/', Wallpaper.as_view(), name='bing'),
    path('/', Wallpaper.as_view(), name='default'),
    path('latest/', Wallpaper.as_view(), name='latest'),
    path('hot/', Wallpaper.as_view(), name='hot'),
    path('toplist/', Wallpaper.as_view(), name='toplist'),
    path('random/', Wallpaper.as_view(), name='random'),
]


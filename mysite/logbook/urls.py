"""mysite URL Configuration

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
from django.urls import path, include
from .views import (
    MovieListView,
    Movie,
    create_movie,
    CinemaListView,
    Cinema,
    create_сinema,
    get_all_hall,
    get_hall_by_id,
    create_hall,
    get_all_Session,
    get_Session_by_id,
    create_Session
                    )

urlpatterns = [
    path('movies/', get_all_Session),
    path('movies/<int:pk>', get_Session_by_id),
    path('movies/create/', create_Session)
]
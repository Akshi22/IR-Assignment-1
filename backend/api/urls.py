from .views import apiOverview, lyricList, search
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('song-list/', views.lyricList, name='song-list'),
    path('search/', views.search, name='Search')
]

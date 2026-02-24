from django.contrib import admin
from django.urls import path, include
from .views import news_list, news_detail, home_page, uzb_page, jahon_page, school_page

urlpatterns = [
    path('', home_page, name='home'),
    path('maktab', school_page, name='maktab'),
    path('jahon', jahon_page, name='jahon'),
    path('uzbekiston', uzb_page, name='uzb'),
    path("news/<int:id>/", news_detail, name='news_detail_page')
]
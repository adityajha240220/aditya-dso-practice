from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("news/", views.news_list, name="news_list"),
    path("news/today/", views.news_today, name="news_today"),
    path("news/category/<str:name>/", views.news_category, name="news_category"),
    path("news/create/", views.news_create, name="news_create"),
    path("news/<slug:slug>/", views.news_detail, name="news_detail"),
]

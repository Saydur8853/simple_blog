from django.urls import path

from post import views

urlpatterns = [
    path("", views.index, name="index"),
    path("weather/", views.weather, name="weather"),
    path("post/<str:pk>", views.post, name="post"),
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.start_new_game, name="start_new_game"),
]
from django.urls import include, path

from . import views

urlpatterns = [
    path("wiki/<entry_name>/", views.entry, name="entry"),
    path("wiki/", views.wiki, name="wiki"),
    path("", views.index, name="index"),
]

from django.urls import include, path

from . import views

urlpatterns = [
    path("results/", views.results, name="results"),
    path("search/", views.search, name="search"),
    path("wiki/<entry_name>/", views.entry, name="entry"),
    path("wiki/", views.wiki, name="wiki"),
    path("", views.index, name="index"),
]

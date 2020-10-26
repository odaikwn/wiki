from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="serachentry"),
    path("add", views.add, name="add"),
    path("create", views.create, name="create"),
    path("<str:name>", views.select, name="selectentry")
]

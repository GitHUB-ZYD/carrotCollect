from django.urls import path

from . import views

urlpatterns = [
    path("", views.myAppModelIndex, name="index"),
    path("getjson", views.returnJsonData, name="json")
]
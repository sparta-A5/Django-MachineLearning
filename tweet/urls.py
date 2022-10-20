from . import views
from django.urls import path

app_name = "tweet"

urlpatterns = [
    path("", views.img_list, name = "img_list"),
    path("pumjong/", views.pumjong, name = "pumjong"),
]
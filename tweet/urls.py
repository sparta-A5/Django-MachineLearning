from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "tweet"

urlpatterns = [
    path("", views.img_list, name = "img_list"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )
from django.urls import path
from user import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
]
from django.urls import path
from . import views
urlpatterns = [
    path('facebook/login', views.fb, name='fb'),
    path('google/login', views.google, name='google'),
]
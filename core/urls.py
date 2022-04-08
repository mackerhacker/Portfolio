from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('mail', views.mail, name="mail")
]

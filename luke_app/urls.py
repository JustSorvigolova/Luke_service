from django.urls import path
from . import views

urlpatterns = [
    path('',  views.DoctorsView_Home.as_view()),
]
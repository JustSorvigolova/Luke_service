from django.urls import path
from . import views

urlpatterns = [
    path('',  views.DoctorsView_Home.as_view(), name="doctor_list_home"),
    path('doctors/',  views.DoctorsView_List.as_view(), name="doctor_list"),
    path('contacts/',  views.Contact.as_view(), name="contacts"),
    path('service/',  views.Service_List.as_view(), name="service"),
    path('news/',  views.NewsView_List.as_view(), name="news"),
    path("<int:pk>", views.NewsView_Detail.as_view(), name="news_detail"),
]
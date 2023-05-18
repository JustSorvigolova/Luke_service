from django.views.generic import ListView, DetailView
from .models import News, Doctor, Service, Photo


class DoctorsView_Home(ListView):
    model = Doctor
    queryset = Doctor.objects.all()[:3]
    template_name = "luke_app/index.html"



# class DoctorsView(ListView):
#     model = Doctor
#     queryset = Doctor.objects.all()[:3]
#     template_name = ""
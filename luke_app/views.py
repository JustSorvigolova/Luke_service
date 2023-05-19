from django.views.generic import ListView, DetailView
from .models import News, Doctor, Service, Service_Massage, Service_Dantist, Service_Ultrasound


class DoctorsView_Home(ListView):
    model = Doctor
    queryset = Doctor.objects.all()[:4]
    template_name = "luke_app/index.html"
    context_object_name = "doctors"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all()[:3]
        return context


class DoctorsView_List(ListView):
    model = Doctor
    queryset = Doctor.objects.all()
    template_name = "luke_app/doctors.html"
    context_object_name = "doctor_list"


class NewsView_List(ListView):
    model = News
    queryset = News.objects.all()
    template_name = "luke_app/news_list.html"
    context_object_name = "news_list"


class NewsView_Detail(DetailView):
    model = News
    slug_field = "id"
    template_name = "luke_app/news_detail.html"
    context_object_name = "news_det"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = News.objects.all()[:3]
        return context


class NewsView_Detail_List(ListView):
    model = News
    queryset = News.objects.all()[:3]
    template_name = "luke_app/news_detail.html"
    context_object_name = "news_list_detail"


class Service_List(ListView):
    model = Service
    template_name = "luke_app/service.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['massages'] = Service_Massage.objects.all()
        context['dantists'] = Service_Dantist.objects.all()
        context['ultrasounds'] = Service_Ultrasound.objects.all()
        return context


class Contact(ListView):
    model = News
    template_name = "luke_app/contact.html"

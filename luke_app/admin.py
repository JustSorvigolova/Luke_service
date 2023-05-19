from django.contrib import admin
from .models import News, Doctor, Service, Service_Ultrasound, Service_Massage, Service_Dantist

admin.site.register(News)
admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(Service_Massage)
admin.site.register(Service_Ultrasound)
admin.site.register(Service_Dantist)

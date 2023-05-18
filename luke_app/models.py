from django.db import models


class News(models.Model):
    """ Новости """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    photos = models.ManyToManyField('Photo', blank=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    """Фото"""
    image = models.ImageField(upload_to='news/')

    def __str__(self):
        return self.image.name


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price_1 = models.DecimalField(max_digits=8, decimal_places=2)
    price_pensioner = models.DecimalField(max_digits=8, decimal_places=2)
    price_WWII = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    """Доктора"""
    Second_Name = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)
    Sur_Name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='doctors/', null=True, blank=True)

    def __str__(self):
        return self.First_Name

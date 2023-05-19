from django.db import models


class News(models.Model):
    """ Новости """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    photo_news = models.ImageField(upload_to='photo/', null=True, blank=False)

    def __str__(self):
        return self.title

    def get_short_content(self):
        # Разделите содержимое на отдельные слова
        words = self.content.split()

        # Верните только первые пять слов (или меньше, если содержимое короче)
        return ' '.join(words[:20])

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    price_discount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга Общая"
        verbose_name_plural = "Услуги_Общие"


class Service_Massage(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга Массаж"
        verbose_name_plural = "Услуги Массажа"


class Service_Dantist(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Стоматологическая услуга"
        verbose_name_plural = "Стоматологические услуги"


class Service_Ultrasound(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    price_discount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга УЗИ"
        verbose_name_plural = "Услуги УЗИ"


class Doctor(models.Model):
    """Доктора"""
    Second_Name = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)
    Sur_Name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='doctors/', null=True, blank=True)
    bio = models.TextField(blank=False)

    def __str__(self):
        return self.First_Name

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"
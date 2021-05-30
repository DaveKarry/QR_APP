from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS_CHOICES = [
    ('New', 'Новый'),
    ('Act', 'Активный'),
    ('Dea', 'Не активный'),
]

class Person(models.Model):
    name = models.CharField(max_length=30)
    sname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)  # отчество
    dateOfBirth = models.DateField()
    adress = models.CharField(max_length=50)
    qr_code = models.ImageField( blank=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='New')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()



    def get_absolute_url(self):
        return reverse("person", kwargs={
            'slug': self.slug
        })

    def get_update_status_url(self):
        return reverse("setStatus", kwargs={
            'slug': self.slug
        })


class News(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=500)
    img = models.ImageField(upload_to="news_image/%Y/%m/%d", blank=True)
    creationDate = models.DateField()
    slug = models.SlugField()

    def get_delete_url(self):
        return reverse("deleteNews", kwargs={
            'slug': self.slug
        })


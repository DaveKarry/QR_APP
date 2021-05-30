import os
import time
import urllib

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.text import slugify
from django.utils import timezone
from django.views import View
from django.views.generic import DetailView

from .forms import *
from .models import *
from random import randint
from django.core.files import File
import qrcode



class Index(View):
    def get(self,*args, **kwargs):
        news = News.objects.order_by()
        return render(self.request, 'QR_app/Index.html', {'news' : news})


class Register(View):
    def get(self, *args, **kwargs):
        form = UserCreationForm()
        context = {'form': form}
        return render(self.request, 'registration/register.html', context)

    def post(self,*args, **kwargs):
        form = UserCreationForm(self.request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(self.request, user)
            time.sleep(1)
            return redirect('index')
        else:
            messages.info(self.request, 'Ошибка регистрации! Проверьте поля!')
            return HttpResponseRedirect('register')


class Out(View):
    def get(self,*args, **kwargs):
        logout(self.request)
        return render(self.request, 'QR_app/Index.html')


class RegisterPerson(View):
    def get(self,*args,**kwargs):
        form = NewPerson()
        print(type(form))
        return render(self.request, 'QR_app/RegisterPerson.html', {'form': form})

    def post(self,*args,**kwargs):
        form = NewPerson(self.request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.user = self.request.user
            slug = person.name + person.sname + str(randint(100,1000))
            person.slug = slugify(slug,allow_unicode=True)
            person.save()
            return redirect('index')

        if self.request.user.is_superuser:
            return redirect('adminPanel')
        else:
            return RegisterPerson(View)


class AdminPanel(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return render(self.request, 'QR_app/admin/admin.html')
        else:
            return render(self.request, 'QR_app/accessError.html')


class PeopleList(View):
    def get(self, *args,**kwargs):
        Plist = Person.objects.order_by('status')
        if self.request.user.is_superuser:
            return render(self.request, 'QR_app/admin/PList.html', {'plist': Plist} )
        else:
            return render(self.request, 'QR_app/accessError.html')


class PersonDetailView(DetailView):
    model = Person
    print(model.qr_code)
    template_name = "QR_app/admin/person.html"


class PersonSetStatus(View):
    def get(self, *args, **kwargs):
        form = PersonSetStatusForm()
        return render(self.request, 'QR_app/admin/update_status.html', {'form': form})
    def post(self, *args, **kwargs):
        form = PersonSetStatusForm(self.request.POST)
        if form.is_valid():
            person = Person.objects.get(slug=kwargs['slug'])
            person.status = form.cleaned_data['status']
            if person.status == 'Act':
                qr_code = qrcode.make([person.name, person.sname, person.adress]) #set contsnt on qr
                image_url = "QR_app/media/QR_CODE " + person.slug + ".png" #set neme on qr
                qr_code.save( image_url )
                local_file = open(image_url, "rb")
                djangofile = File(local_file)
                person.qr_code.save(image_url, djangofile,save=True)
                local_file.close()
            person.save()
            Plist = Person.objects.order_by('status')
            return redirect('PList')


class AddNews(View):
    def get(self,*args,**kwargs):
        form = AddNewsForm()
        return render(self.request, "QR_app/admin/addnews.html", {'form' : form})
    def post(self, *args, ** kwargs):
        form = AddNewsForm(self.request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.creationDate = timezone.now()
            slug = news.title + str(news.creationDate) + str(randint(0,100))
            news.slug =  slugify(slug,allow_unicode=True)
            news.save()
            return redirect('index')
        else:
            print("error. News cant construct")
            return render(self.request, 'QR_app/admin/admin.html')

class DeleteNews(View):
    def get(self, *args, **kwargs):
        news = get_object_or_404(News, slug=kwargs['slug'])
        news.delete()
        return redirect('index')

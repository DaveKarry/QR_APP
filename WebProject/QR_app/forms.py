from django import forms
from .models import *


class NewPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name','sname', 'patronymic', 'dateOfBirth', 'adress',)


class PersonSetStatusForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('status',)


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title','content', 'img',)
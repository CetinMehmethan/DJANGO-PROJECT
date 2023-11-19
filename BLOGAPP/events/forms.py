from django import forms
from django.forms import TextInput, Textarea

from .models import events

class EventCreateForm(forms.ModelForm):
       class Meta:
           model = events
           fields = '__all__'
           label = {
               "title":"Etkinlik Adı :",
               "description":"Açıklama :",
               "isActive":"Aktif Kurs",
           }
           widgets = {
               "title" :TextInput(attrs = {"class":"form-control"}),
               "subtitle" :TextInput(attrs = {"class":"form-control"}),
               "Description": Textarea(attrs={"class": "form-control"}),
               "slug": TextInput(attrs={"class": "form-control"}),
           }


class EventEditForm(forms.ModelForm):
    class Meta:
        model = events
        fields = '__all__'
        label = {
            "title": "Etkinlik Adı :",
            "description": "Açıklama :",
            "isActive": "Aktif Kurs",
        }
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "description": Textarea(attrs={"class": "form-control"}),
            "slug": TextInput(attrs={"class": "form-control"}),
        }

class UploadForm(forms.Form):
    image = forms.ImageField()





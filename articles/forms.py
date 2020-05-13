from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article #defining our form and the fields 
        fields = ['title', 'body', 'slug', 'thumb']
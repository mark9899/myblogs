from.models import Blog_Category
#from django import forms
from django.forms import ModelForm


class Blog_Form(ModelForm):
    class Meta:
         model = Blog_Category
         fields = "__all__"

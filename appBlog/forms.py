from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','text']
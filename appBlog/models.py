from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title=models.CharField(("Başlık"), max_length=50)
    content=models.TextField(("İçerik"),max_length=1000)
    date=models.DateTimeField(("Tarih-Saat"), auto_now_add=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post=models.ForeignKey(Post, verbose_name=("comments"), on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(("İsim"), max_length=50)
    email=models.EmailField(("E-mail"), max_length=254)
    text=models.TextField(("Mesaj"),max_length=1000)
    date_added=models.DateTimeField(("Tarih-Saat"), default=timezone.now)

    def __str__(self):
        return f'Comment by {self.name}'
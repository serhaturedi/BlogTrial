"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appBlog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='index'),
    path('post/<int:id>/',post_detail,name='post_detail'),
    path('post/new/',post_new,name='post_new'),
    path('post/<int:id>/edit/',post_edit,name='post_edit'),
    path('post/<int:id>/delete/',post_delete,name='post_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

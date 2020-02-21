from django.contrib import admin
from django.urls import path
from . import views

urlpattern = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
]
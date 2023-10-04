from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('home/', views.home,name='home'),
    path('home/bt1.html', views.baitap_1, name='bt1'),
    path('home/bt2.html', views.baitap_2, name='bt2'),
    path('home/bt3.html', views.baitap_3, name='bt3'),
    path('home/bt4.html', views.baitap_4, name='bt4'),
    path('home/bt5.html', views.baitap_5, name='bt5'),

]
from django.conf.urls.static import static
from django.conf import settings
# Add the following lines to serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
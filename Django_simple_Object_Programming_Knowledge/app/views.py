from django.shortcuts import render
from .models import KHAINIEM, BAITAP
from django.http import HttpResponse
# Create your views here.

def home(request):
    khainiem_objects = KHAINIEM.objects.all()
    baitap_objects = BAITAP.objects.all()
    context = {'khainiem_objects': khainiem_objects, 'baitap_objects': baitap_objects}
    return render(request, 'home.html', context)

def baitap_1(request):
    # Your existing logic for the 'baitap_1' view
    return render(request, 'bt1.html')
def baitap_2(request):
    return render(request, 'bt2.html')
def baitap_3(request):
    return render(request, 'bt3.html')

def baitap_4(request):
    return render(request, 'bt4.html')

def baitap_5(request):
    return render(request, 'bt5.html')



def get_nd(request):
    # Get the object with MA_KNIEM = 'nd1' or return 404 if not found
    nd = get_object_or_404(KHAINIEM, MA_KNIEM='nd1')
    context = {'nd': nd}
    return render(request, 'home.html', context)



from django.shortcuts import render
from django.http import HttpResponse

from appwebsite.models import CompanyInfo


# Create your views here.

def about(request):
    context ={
        'name':'clif'
    }
    return render(request,'appwebsite/about.html',context)
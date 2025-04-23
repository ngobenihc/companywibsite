from django.shortcuts import render
from django.http import HttpResponse

from appwebsite.models import CompanyInfo


# Create your views here.
def home(request):
    return render(request, 'appwebsite/home.html', )

def about(request):
    context ={
        'name':'clif'
    }
    return render(request,'appwebsite/about.html',context)




def testimonials(request):
    return render(request, 'appwebsite/testimonials.html', )
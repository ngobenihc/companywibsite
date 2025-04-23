from django.shortcuts import render
from django.http import HttpResponse

from appwebsite.models import CompanyInfo


# Create your views here.
def home(request):
    company = CompanyInfo.objects.first()
    context = {
    'company_name':company.company_name,
    "location":company.location,
    'phone':company.phone,
    'email': company.email,
    'open_hours':company.open_hours,
    'video_url': company.video_url,
    'twitter_url': company.twitter_url,
    'instagram_url':company.instagram_url,
    'linkedin_url': company.linkedin_url,
    'facebook_url':company.facebook_url,
    }
    return render(request, 'appwebsite/home.html', context)

def about(request):
    context ={

    }
    return render(request,'appwebsite/about.html',context)

def testimonials(request):

    return render(request, 'appwebsite/testimonials.html', )
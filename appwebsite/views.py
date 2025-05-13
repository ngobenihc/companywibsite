from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings

from appwebsite.models import CompanyInfo, ServiceInfo, TestimonialIfor, FrequentlyAskedQuestionsInfo, BlogInfo


# Create your views here.
def home(request):
    company = CompanyInfo.objects.first()
    service = ServiceInfo.objects.all()
    testimonial = TestimonialIfor.objects.all()
    asked_questions = FrequentlyAskedQuestionsInfo.objects.all()
    blog_post = BlogInfo.objects.all().order_by("-date_created")[:3]
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
    'service': service,
    'testimonial':testimonial,
    'asked_questions':asked_questions,
    'blog_post':blog_post,
    }
    return render(request, 'appwebsite/home.html', context)


def about(request):
    context ={

    }
    return render(request,'appwebsite/about.html',context)


def testimonials(request):
    testimonial = TestimonialIfor.objects.all()
    context = {
        'testimonial':testimonial,
    }

    return render(request, 'appwebsite/testimonials.html',context )


def services(request):
    service =ServiceInfo.objects.all()
    context = {
        'icon':service.icon,
        'title':service.tittle,
        'description':service.description,

    }
    return render(request, 'appwebsite/testimonials.html',context )


def contact_form(request):

    if request.method =='POST':

        name=request.POST.get('name')
        email=request.POST.get('email')
        subject = request.POST.get('subject')
        message=request.POST.get('message')

    context ={

    }
    send_mail(
        subject=subject,
        message=f'{name} {email} {message}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=False

    )
    return redirect('home-page')


def blog(request):
    testimonial = TestimonialIfor.objects.all()
    blog_post = BlogInfo.objects.all().order_by("-date_created")[:3]
    context = {
        'testimonial':testimonial,
        'blog_post': blog_post,
    }

    return render(request, 'appwebsite/blog.html',context )



def blog_details(request, blog_id):

    blog_post = BlogInfo.objects.get(id = blog_id)
    context = {

        'blog_post': blog_post,
    }

    return render(request, 'appwebsite/blog_details.html',context )
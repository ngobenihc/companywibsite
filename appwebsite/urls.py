from django.contrib import admin

from . import views
from django.urls import path

from .views import blog_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home-page'),
    path('about/',views.about,name='about-page'),
    path('test/',views.testimonials,name ='testimonials'),
    path('contact/',views.contact_form,name='contact-page'),
    path('details/<blog_id>',blog_details,name='blog-page'),
]
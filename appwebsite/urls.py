from . import views
from django.urls import path



urlpatterns = [
    path('',views.home,name='home-page'),
    path('about/',views.about,name='about-page'),
    path('test/',views.testimonials,name ='testimonials'),
]
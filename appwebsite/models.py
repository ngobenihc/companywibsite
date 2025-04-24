from django.db import models

# Create your models here.
class CompanyInfo(models.Model):
    company_name =models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    phone =models.CharField(max_length=255)
    email =models.EmailField()
    open_hours =models.CharField(max_length=150,blank=True,null=True)
    video_url = models.URLField(blank=True,null=True)
    twitter_url = models.URLField(blank=True,null=True)
    instagram_url = models.URLField(blank=True,null=True)
    linkedin_url = models.URLField(blank=True,null=True)
    facebook_url = models.URLField(blank=True,null=True)



    def __str__(self):
        return f'{self.company_name} company profile'




class ServiceInfo(models.Model):
    icon = models.CharField(max_length=100,blank=True)
    tittle = models.CharField(max_length=200,unique=True)
    description =models.TextField()


    def __str__(self):
        return f'{self.tittle} tittle profile'
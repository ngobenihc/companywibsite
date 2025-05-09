from django.db import models
from django.utils import timezone

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


class TestimonialIfor(models.Model):
    img = models.CharField(max_length=255,blank=True,null=True)
    num_stars =[(1,'One'),
                (2,'Two'),
                (3,'Three'),
                (4,'Four'),
                (5,'Five')]

    count_rating = models.IntegerField(choices=num_stars)
    user_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=150)
    description_review = models.TextField()



    def __str__(self):
        return f'{self.user_name} user profile'


class FrequentlyAskedQuestionsInfo(models.Model):
    questions = models.CharField(max_length=255)
    answer= models.TextField()

    def __str__(self):
        return f'{self.questions}.. Frequently Asked Questions'

class ContactInfo(models.Model):
    name = models.CharField(max_length=255)
    email= models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    action_time =models.DateTimeField(null=True,blank=True)
    is_succesful = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)
    error_message = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.email}.. user email'


class AuthorInfor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    joined_date = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return f'{self.first_name}.. user name'



class BlogInfo(models.Model):
    img = models.CharField(max_length=255,null=True,blank=True)
    topic= models.CharField(max_length=255,null=True,blank=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(AuthorInfor,null=True, on_delete=models.CASCADE)
    context = models.TextField(null=True)
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.date_created}.. the writer of the blog'


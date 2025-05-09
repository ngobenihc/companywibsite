from django.contrib import admin

from appwebsite.models import CompanyInfo, ServiceInfo, TestimonialIfor, FrequentlyAskedQuestionsInfo, BlogInfo, \
    ContactInfo, AuthorInfor


# Register your models here.
#admin.site.register(CompanyInfo)


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = [
        'company_name',
        'location',
        'phone',
        'email',
        'open_hours'
    ]

    search_fields = [
        'company_name'
    ]
    # def has_add_permission(self, request):
    #     return False
    # def has_change_permission(self, request, obj=None):
    #     return False
    # def has_delete_permission(self, request, obj=None):
    #     return False
    # readonly_fields = [
    #     'company_name'
    # ]


@admin.register(ServiceInfo)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'tittle',
        'description',
    ]

    search_fields = [
        'tittle'
    ]


@admin.register(TestimonialIfor)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = [
        'user_name',
        'job_title',
        'display_count'
    ]


    def display_count(self,obj):
        return '*' * obj.count_rating
    display_count.short_description = 'Rating'



@admin.register(FrequentlyAskedQuestionsInfo)
class FrequentlyAskedQuestionsInfoAdmin(admin.ModelAdmin):
    list_display = [
        'questions',
        'answer',
    ]


@admin.register( ContactInfo)
class  ContactInfoAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
    ]

@admin.register(BlogInfo)
class BlogInfoAdmin(admin.ModelAdmin):
    list_display = [

        'title',
        'topic',
    ]

@admin.register(AuthorInfor)
class AuthorInforAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'country',
    ]
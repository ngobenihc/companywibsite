from django.contrib import admin

from appwebsite.models import CompanyInfo, ServiceInfo


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
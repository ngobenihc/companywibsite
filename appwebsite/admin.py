from django.contrib import admin

from appwebsite.models import CompanyInfo

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


    # def has_add_permission(self, request):
    #     return False
    # def has_change_permission(self, request, obj=None):
    #     return False
    # def has_delete_permission(self, request, obj=None):
    #     return False
    # readonly_fields = [
    #     'company_name'
    # ]
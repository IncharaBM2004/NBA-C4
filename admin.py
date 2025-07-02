from django.contrib import admin
from .models import AdmissionDetails, Students,company_info

# Register models
admin.site.register(AdmissionDetails)
admin.site.register(Students)
admin.site.register(company_info)



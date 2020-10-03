from django.contrib import admin
from .models import User,DeveloperProfile,CompanyProfile





admin.site.register(User)
admin.site.register(DeveloperProfile)
admin.site.register(CompanyProfile)
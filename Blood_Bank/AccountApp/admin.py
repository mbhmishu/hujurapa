from django.contrib import admin
from .models import User, DonerRequest,PatientInfo,UserProPic,OrgInfo
# Register your models here
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")

@admin.register(DonerRequest)
class DonerRequestAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")

@admin.register(PatientInfo)
class PatientInfoAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")


@admin.register(OrgInfo)
class OrgInfoAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")

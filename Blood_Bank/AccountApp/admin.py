from django.contrib import admin
from .models import User, DonerRequest,PatientInfo,UserProPic,OrgInfo
# Register your models here
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =  ('username','first_name','last_name', 'password', 'email','is_patient','is_Org')



@admin.register(PatientInfo)
class PatientInfoAdmin(admin.ModelAdmin):
    list_display = ("user", "date_of_birth", "blood_group", "Gender", "weight", "height","phone_no","locations","website","fb","tw","instra","pres_address","parmanent_address","bio")



admin.site.register(OrgInfo)

admin.site.register(UserProPic)




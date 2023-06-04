from django.urls import path
from AccountApp import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'Accountapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('regi_type/', views.regi_type, name='regi_type'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('patient_regi/', views.patient_regi, name='patient_regi'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('patient_profile/<username>/', views.patient_profile, name='patient_profile'),
    path('patient_edit_pro/', views.patient_edit_pro, name='patient_edit_pro'),
    path('ChangePasss/', views.ChangePasss, name='ChangePasss'),
    path('ChangeUser/', views.ChangeUser, name='ChangeUser'),
    path('AddProPic/', views.AddProPic, name='AddProPic'),
    path('ProPicChange/', views.ProPicChange, name='ProPicChange'),
    path('hospital_regi/', views.org_regi, name='hospital_regi'),#Org Registration 

    path('ORG_dashboard/', views.ORG_dashboard, name='ORG_dashboard'),
    path('ORG_edit_pro/', views.ORG_edit_pro, name='ORG_edit_pro'),
    path('review/', views.review, name='review'),
    path('search_all/', views.search_all, name='search'),
    path('view_all_profile/<username>/', views.view_all_profile, name='view_all_profile'),
    path('ORG_details/<username>/', views.org_profile, name='ORG_details'),
    path('notfound',views.notfound, name='notfound'),
    path('send_donor_request/<username>/', views.send_donor_request, name='send_donor_request'),  

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

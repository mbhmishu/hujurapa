from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_patient = models.BooleanField('Is patient', default=False)
    is_Org = models.BooleanField('Is Org', default=False)
    

BloodGroup=(

    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
    ('O+','O+'),
    ('O-','O-'),
)



gander = (
    ('Maile','Maile'),
    ('Femail','Femail'),

)

#user info models_module

class UserProPic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    proPic = models.ImageField(upload_to='user_profile_pic', blank=True, null=True)


class PatientInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_info')
    date_of_birth= models.DateField(blank=True, null=True)
    blood_group =models.CharField( max_length=5, choices=BloodGroup)
    Gender = models.CharField(choices=gander, max_length=24)
    weight = models.CharField( max_length=24,blank=True, null=True)
    height = models.CharField( max_length=24,blank=True, null=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    locations = models.CharField(max_length=300, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    fb = models.URLField(blank=True, null=True)
    tw = models.URLField(blank=True, null=True)
    instra = models.URLField(blank=True, null=True)
    pres_address = models.CharField(max_length=264, blank=True, null=True)
    parmanent_address = models.CharField(max_length=264, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.user.username


class OrgInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='org_info')
    RegiNo =models.CharField(unique=True, max_length=30, null=True, blank=True)
    org_type = models.CharField( max_length=264, blank=True, null=True)
    division =models.CharField( max_length=24 , blank=True, null=True)
    district = models.CharField(max_length=24, blank=True, null=True)
    upazilla = models.CharField(max_length=24, blank=True, null=True)
    last_updated_regi = models.DateField(null=True, blank=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    services= models.CharField(max_length=264, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    fb = models.URLField(blank=True, null=True)
    tw = models.URLField(blank=True, null=True)
    instra = models.URLField(blank=True, null=True)
    pres_address = models.CharField(max_length=264, blank=True, null=True)
    parmanent_address = models.CharField(max_length=264, blank=True, null=True)


    def __str__(self):
        return self.user.username
    





class Review(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_receiver')
    giver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_giver')
    review=models.TextField()
    review_date=models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-review_date',]
    
    def __str__(self):
        return self.review


class ReviewLikes(models.Model):
    Review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='like_Review')
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likers')

    def __str__(self):
        return self.user + 'likes' + self.Review
    



activitys = (
    (None, 'Select'),
    ('ACCEPT', 'ACCEPT'),
    ('REJECT', 'REJECT'),  
)
class DonerRequest(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='donor',null=True, blank=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Recipient')
    stutas = models.CharField(max_length=10, choices=activitys, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)







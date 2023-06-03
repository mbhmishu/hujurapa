from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from AccountApp.models import User,UserProPic,PatientInfo,OrgInfo,Review,ReviewLikes,DonerRequest


# Rgistratuon forms ######################
class Patien_RegisForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'usernam'}),label='')
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),label='')
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),label='')
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label='')
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),label='')
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'@Email'}),label='')
    is_patient = forms.BooleanField(required=True , label='Im a patient')

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1', 'password2', 'email','is_patient')


class Org_RegisForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'usernam'}),label='')
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),label='')
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),label='')
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label='')
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),label='')
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'@Email'}),label='')
    is_Org = forms.BooleanField(required=True , label='Is Organization')

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1', 'password2', 'email','is_Org')



#Login Form #################################
class User_SignInForm(AuthenticationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'usernam'}),label='username')
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label='Password')
    
    class Meta:
        model = User
        fields = ('username', 'password')



# Profile Ssting Form ##########################
class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','password')

class PatientInfoEdForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='Date of birth',widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = PatientInfo
        exclude = ('user',)

class ORG_InfoEdForm(forms.ModelForm):
    last_updated_regi = forms.DateField(label='Date of birth',widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = OrgInfo
        exclude = ('user',)

class UserProPicForm(forms.ModelForm):
    class Meta:
        model = UserProPic
        fields = ['proPic']



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review',)




activitys = (
    (None, 'Select Blood Group'),
    ('ACCEPT', 'ACCEPT'),
    ('REJECT', 'REJECT'),  
)
class DonorForm(forms.ModelForm):
    class Meta:
        model = DonerRequest
        fields = ('stutas',)
        widgets = {
            'stutas': forms.Select(choices=activitys),
        }



      



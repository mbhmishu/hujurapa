from django.shortcuts import render,redirect ,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from AccountApp.forms import UserProPicForm,Patien_RegisForm,Org_RegisForm,UserEditForm,User_SignInForm, PatientInfoEdForm,ORG_InfoEdForm,ReviewForm,DonorForm
from AccountApp.models import User,UserProPic,PatientInfo,OrgInfo,ReviewLikes,Review,DonerRequest
from django.contrib.auth.forms import AuthenticationForm,  UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView

from blogapp.models import Follow






# SineUp views ####################################

def regi_type(request):
    return render(request, 'Account/register_type.html', context={})


def patient_regi(request):
    registerd = False
    form = Patien_RegisForm()
    if request.method == 'POST':
        form = Patien_RegisForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            registerd = True
            user_profile = PatientInfo(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('Accountapp:sign_in'))  
    return render (request, 'Account/patient_regi.html', context={'form':form , 'registerd':registerd}) 


def org_regi(request):
    form = Org_RegisForm()
    if request.method == 'POST':
        form = Org_RegisForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = OrgInfo(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('Accountapp:sign_in')) 
    return render(request, 'Account/hospital_regi.html', context={'form': form})



#SignIn SignOut views ###################################  
def sign_in(request):
    form = User_SignInForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_patient:
                login(request, user)
                return HttpResponseRedirect(reverse('Accountapp:patient_dashboard'))
            elif user is not None and user.is_Org:
                login(request, user)
                return HttpResponseRedirect(reverse('Accountapp:ORG_dashboard')) 
            return HttpResponseRedirect(reverse('Accountapp:notfound'))
    return render(request,'Account/login.html', context={'form':form, 'title':'Login'})


@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('Accountapp:sign_in'))

  
def index(request):
    return render(request, 'Account/base.html')

def notfound(request):
    return render(request, 'notfound.html')



#Profile details views 
@login_required
def org_profile(request, username):
    result_user = User.objects.get(username=username)
    reviews = Review.objects.filter(receiver__username=username)
    donor_request = DonerRequest.objects.filter(donor=request.user).count()
    review_form = ReviewForm()
    donor_accept_rejects = DonorForm()
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.giver = request.user
            review.receiver = result_user
            review.save()
            return HttpResponseRedirect(reverse('Accountapp:ORG_details' , kwargs={'username':username}))
    return render(request, 'org_details.html', context={'result_user':result_user, 'review_form':review_form,'donor_request':donor_request})  
    

@login_required
def patient_profile(request, username):
    result_user = User.objects.get(username=username)
    reviews = Review.objects.filter(receiver__username=username)
    review_form = ReviewForm()

    alrady_request = DonerRequest.objects.filter(donor__username=username)
    if alrady_request:
        donor_request = True
    else:
        donor_request = False

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.giver = request.user
            review.receiver = result_user
            review.save()
            return HttpResponseRedirect(reverse('Accountapp:patient_profile' , kwargs={'username':username}))
    return render(request, 'org_details.html', context={'result_user':result_user, 'review_form':review_form,'donor_request':donor_request})  
    

    
#Donor management
@login_required
def send_donor_request(request, username):
    donor_user=User.objects.get(username=username)
    alr_request = DonerRequest.objects.filter(donor__username=username)
    if not alr_request:
        donor_re = DonerRequest(donor=donor_user,recipient=request.user,stutas='Select')
        donor_re.save()
        donor_request = True
        return HttpResponseRedirect(reverse('Accountapp:patient_profile' , kwargs={'username':username}))
    return HttpResponseRedirect(reverse('Accountapp:patient_profile' , kwargs={'username':username}))


#User dashboard views ##############################
@login_required
def patient_dashboard(request):
    blood_request= DonerRequest.objects.filter(donor=request.user)
    donors = DonerRequest.objects.filter(donor=request.user)
    form=DonorForm()
    if request.method == 'POST':
        donor = donors.first() 
        form = DonorForm(request.POST or None, instance=donor)
        if form.is_valid():
            donet=form.save()
            if donet.stutas=='REJECT':
                donet.delete()
                return HttpResponseRedirect(reverse('Accountapp:patient_dashboard'))
            return HttpResponseRedirect(reverse('Accountapp:patient_dashboard'))
    if request.method == "GET":
        Search = request.GET.get('Search', '')
        results = User.objects.filter(username__icontains=Search)[0:1]
        
    return render(request, 'Profile/patient_dashboard.html', context={'blood_request': blood_request,'form':form,'results':results,'Search':Search})


@login_required
def ORG_dashboard(request):
    if request.method == "GET":
        Search = request.GET.get('Search', '')
        results = User.objects.filter(username__icontains=Search)[0:1]
    return render(request, 'Profile/org_dashboard.html', context={'results':results,'Search':Search})



@login_required
def review(request):
    return render(request, 'reviews.html', context={})



# Search List View
@login_required
def search_all(request):
    user_list = User.objects.order_by('username')
    if request.method == "GET":
        Search = request.GET.get('Search', '')
        results = User.objects.filter(username__icontains=Search)
    return render(request, 'search.html', context={'results': results, 'Search': Search,'user_list':user_list})


@login_required
def view_all_profile(request, username):
    result_user = User.objects.get(username=username)
    if result_user.is_patient:
        if result_user == request.user:
            return HttpResponseRedirect(reverse('Accountapp:patient_dashboard'))
        return HttpResponseRedirect(reverse('Accountapp:patient_profile' , kwargs={'username':username}))  
    if result_user.is_Org:
        if result_user == request.user:
            return HttpResponseRedirect(reverse('Accountapp:ORG_dashboard'))
        return HttpResponseRedirect(reverse('Accountapp:ORG_details' , kwargs={'username':username}))       
         
    return HttpResponseRedirect(reverse('Accountapp:notfound'))




  
    


# user_profile_settings #################
@login_required
def patient_edit_pro(request):
    current_user = PatientInfo.objects.get(user=request.user)
    form = PatientInfoEdForm(instance=current_user)
    if request.method == "POST":
        form = PatientInfoEdForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = PatientInfoEdForm(instance=current_user)
            return HttpResponseRedirect(reverse('Accountapp:patient_dashboard'))
    return render(request, 'Profile/patient_profile_settings.html', context={'form':form})





@login_required 
def ORG_edit_pro(request):
    current_user = OrgInfo.objects.get(user=request.user)
    form = ORG_InfoEdForm(instance=current_user)
    if request.method == 'POST':
        form = ORG_InfoEdForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Accountapp:ORG_dashboard'))
    return render(request, 'Profile/patient_profile_settings.html', context={'form':form})




@login_required
def ChangePasss(request):
    ps_msg = False
    current_user = request.user
    Change_passowrd = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, request.POST,)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Accountapp:index'))       
    return render(request,'Account/change_pass.html', context={'Change_passowrd':Change_passowrd})


@login_required
def ChangeUser(request):
    u_msg = False
    current_user = request.user
    form = UserEditForm(instance=current_user)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserEditForm(instance=current_user)
            
            if current_user.is_patient:
                return HttpResponseRedirect(reverse('Accountapp:patient_dashboard'))
            elif current_user.is_Org:
                return HttpResponseRedirect(reverse('Accountapp:ORG_dashboard'))
            return HttpResponseRedirect(reverse('Accountapp:notfound'))
    return render(request,'Account/change_user.html', context={'form':form})












# user_profile_pic_settings ##############################

@login_required
def AddProPic(request):
    current_user = request.user
    form = UserProPicForm()
    if request.method=='POST':
        form=UserProPicForm(request.POST, request.FILES)
        if form.is_valid():
            user_obj=form.save(commit=False)
            user_obj.user=request.user
            user_obj.save()
            
            if current_user.is_patient:
                return HttpResponseRedirect(reverse('Accountapp:patient_dashboard'))
            elif current_user.is_Org:
                return HttpResponseRedirect(reverse('Accountapp:ORG_dashboard'))
            return HttpResponseRedirect(reverse('Accountapp:notfound'))
    return render(request,'Account/ProfilePicForm.html', context={'form':form})


def ProPicChange(request):
    current_user = request.user
    cp_msg = False
    form = UserProPicForm(instance=request.user.user_profile)
    if request.method == 'POST':
        form = UserProPicForm(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            cp_msg = True
            if current_user.is_patient:
                return HttpResponseRedirect(reverse('Accountapp:patient_dashboard'))
            
            elif current_user.is_Org :
                return HttpResponseRedirect(reverse('Accountapp:ORG_dashboard'))
            
            return HttpResponseRedirect(reverse('Accountapp:notfound'))      
    return render(request,'Account/ProfilePicForm.html', context={'form':form})







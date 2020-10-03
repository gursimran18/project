from django.shortcuts import render,HttpResponse
from account.models import DeveloperProfile,User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile(request):
    return render(request,'developer/profile.html')


@login_required
def createprofile(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        address = request.POST['address']
        phone = request.POST['phone']
        currentjob = request.POST['currentjob']
        company = request.POST['currentcompany']
        dob = request.POST['dob']
        
        try:
            profile = DeveloperProfile.objects.get(developer_id=request.user.id)


            profile.first_name = fname
            profile.last_name = lname
            
            profile.address = address
            profile.phone = phone
            profile.birthDate = dob
            profile.current_job = currentjob
            profile.company = company
            profile.save()
            return render(request,'developer/profile.html')

        except DeveloperProfile.DoesNotExist:
            DeveloperProfile.objects.create(
            first_name = fname,
            last_name = lname,
            
            address = address,
            phone = phone,
            birthDate = dob,
            current_job_role = currentjob,
            current_company = company,
            developer_id=request.user.id
            ).save()
            return render(request,'developer/profile.html')
    else:
        
        return render(request,'developer/createprofile.html')

    
    



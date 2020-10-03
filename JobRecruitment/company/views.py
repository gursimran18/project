from django.shortcuts import render,HttpResponse,redirect
from account.models import CompanyProfile,User
from django.contrib.auth.decorators import login_required
from .models import Job
from django.contrib import messages
# Create your views here.


@login_required
def homecom(request):
    return render(request,'company/home.html')

#for company profile details filling along with editing
@login_required
def createprofile(request):
    if request.method == "POST":
        cname = request.POST['companyname']
        
        address = request.POST['address']
        phone = request.POST['phone']
        if (CompanyProfile.objects.filter(company_name=request.POST['companyname']).exists()):
            messages.error(request,'this company name  already registered')
            return render(request,'company/createprofile.html')

        
        
        CompanyProfile.objects.create(
        company_name = cname,
        company_address = address,
        company_phone = phone,
        company_id=request.user.id
        ).save()
        return redirect('homecom')
    else:    
        return render(request,'company/createprofile.html')

#company job vacancy adding 

@login_required  
def addjob(request):
    
    if request.method == "POST":
        job_name = request.POST['job_name']
        job_description = request.POST['job_description']
        salary = request.POST['salary']
        job_location = request.POST['location']
        skillsReqd = request.POST['skill_required_1']
        deadline = request.POST['deadline']

        try:
            company_profile = CompanyProfile.objects.get(company_id=request.user.id)
            Job.objects.create(
                job_name=job_name,
                job_description=job_description,
                salary=salary,
                location=job_location,
                skillsReqd=skillsReqd,
                deadline=deadline,
                jobCompany_id=company_profile.id
            ).save()

            messages.success(request, 'Job Vacancy Created')
            return redirect('homecom')

        except CompanyProfile.DoesNotExist:
            messages.warning(request, 'You Must Complete Your Profile Before Creating Job')
            return render(request, 'company/addjob.html')

    else:
        return render(request, 'company/addjob.html')

#where company can view all job vacancies it posted and can edit it,delete,view appicant
def managejobs(request):

    try:
        company_profile = CompanyProfile.objects.get(company_id=request.user.id)
        jobList = Job.objects.filter(jobCompany_id = company_profile.id)
        context = {'jobs': jobList}

    except:
        jobList = []
        context = {'jobs':jobList}

    return render(request,'company/managejob.html',context)
@login_required
#to delete a particular job
def deletejob(request,id):
    company_profile = CompanyProfile.objects.get(company_id=request.user.id)
    item=Job.objects.get(pk=id)

    if str(item.jobCompany) == str(company_profile.company_name):
        item.delete()
        return redirect('managejobs')
    else:
        messages.warning(request, 'you are not authorized to delete')
        return redirect('homecom')

#to view a particular job
def viewjob(request,id):
    
    item=Job.objects.get(pk=id)
    context = {'viewjob':item}
    return render(request,'company/jobdetails.html',context)

@login_required
#to edit a particuar job
def editjob(request,id):

    if request.method=='POST':
        job_name = request.POST.get('job_name')
        job_description = request.POST.get('job_description')
        salary = request.POST.get('salary')
        job_location = request.POST.get('location')
        skillsReqd = request.POST.get('skill_required_1')
        deadline = request.POST.get('deadline')
        try:
            job=Job.objects.get(pk=id)
            job.job_name=job_name
            job.job_description=job_description
            job.salary=salary
            job.location=job_location
            job.skillsReqd=skillsReqd
            job.deadline=deadline
            job.save()
            messages.success(request, 'Job Details have been changed')
            return redirect('managejobs')
        except Exception as e:
            messages.error(request, 'Error Occurred Try again')
            item=Job.objects.get(pk=id)
            context = {'editjob':item}
            return render(request,'company/editjob.html',context)


    item=Job.objects.get(pk=id)
    context = {'editjob':item}
    return render(request,'company/editjob.html',context)
    



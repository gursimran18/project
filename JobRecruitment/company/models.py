from django.db import models
from account.models import CompanyProfile

# job models
class Job(models.Model):
    job_name = models.CharField(max_length=255)
    job_description = models.CharField(max_length=1000)
    salary = models.IntegerField()
    location = models.CharField(max_length=255)
    skillsReqd = models.CharField(max_length=255)
    deadline = models.DateField()
    posted_date = models.DateField(auto_now_add=True)
    jobCompany = models.ForeignKey(CompanyProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.job_name

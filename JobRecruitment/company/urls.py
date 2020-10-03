from django.urls import path,include
from company import views

urlpatterns = [
    path('createprofile',views.createprofile,name="createprofilecom"),
    path('home',views.homecom,name="homecom"),
    path('addjob',views.addjob,name="addjob"),
    path('managejobs',views.managejobs,name="managejobs"),
    path('deletejob/<int:id>',views.deletejob,name="deletejob"),
    path('viewjob/<int:id>',views.viewjob,name="viewjob"),
    path('editjob/<int:id>',views.editjob,name="editjob"),
]
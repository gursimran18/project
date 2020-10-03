from django.urls import path,include
from developer import views

urlpatterns = [
    path('createprofile',views.createprofile,name="createprofiledev"),
    path('home',views.profile,name="profiledev"),
]
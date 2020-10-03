from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserManager(BaseUserManager):

    def create_user(self,email,password=None,is_active=True,is_recruiter = False, is_seeker = False, is_staff=False, is_admin= False):

        if not email:
            raise ValueError("User must have a valid email address")

        if not password:
            raise ValueError("User must have a password")

        user_obj = self.model(

            email = self.normalize_email(email)
        )

        user_obj.set_password(password)

        user_obj.is_active = is_active

        user_obj.is_recruiter = is_recruiter

        user_obj.is_seeker = is_seeker

        user_obj.is_admin = is_admin

        user_obj.is_staff = is_staff

        user_obj.save(using=self._db)

        return  user_obj


    def create_staffuser(self,email,password):
        user = self.create_user(
            email,
            password,
            is_staff=True
        )
        return user


    def create_superuser(self,email,password=None):
        user = self.create_user(
            email,
            password,
            is_admin=True,
            is_staff=True
        )

        return user





class User(AbstractBaseUser):
    email = models.EmailField(

        verbose_name='Email Address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_company = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    registerDate = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self):
        return  self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True



class DeveloperProfile(models.Model):
    developer = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    phone = models.IntegerField()
    dob = models.DateField()
    currentJobName = models.CharField(max_length=255)
    currentCompany = models.CharField(max_length=255)



    def __str__(self):
        return self.first_name


class CompanyProfile(models.Model):

    

    company = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    company_phone = models.IntegerField()
    

    def __str__(self):
        return self.company_name






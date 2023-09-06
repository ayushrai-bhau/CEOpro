from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError




class Company(models.Model):
    compy = models.CharField(max_length=124, null=True, blank=True)
    # created = models.DateTimeField(auto_now_add=True )
    # updated = models.DateTimeField(auto_now=True )
    # deleted = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return str(self.compy)
    

class Myuser(AbstractUser):
    username=None
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True)
    full_name= models.CharField(max_length=250, blank=True, null=True)
    compy =  models.ForeignKey(Company , on_delete=models.CASCADE , blank=True , null= True)
    dob = models.DateField(null=True,blank=True)
    state = models.CharField(max_length=250, blank=True, null=True)
    address = models.TextField(max_length=255, blank=True, null=True)
    phone_number = models.CharField( max_length=50, blank=True, null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_ceo =   models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    # def save(self, *args, **kwargs):
    #     if not self.id and not Myuser.objects.exists():
           
    #         self.is_ceo = True

    # # def company_check(self,):
    #     if self.compy.compy  and self.email:
    #         compy_name = self.compy.compy.lower()+'.com'
    #         domain = self.email.split('@')[1].lower()
    #         if domain != compy_name:
    #             raise ValidationError(f"The email domain '{domain}' does not match the company name '{compy_name}'.")
    #     super().save(*args, **kwargs)

    

    def __str__(self):
        return str(self.full_name)
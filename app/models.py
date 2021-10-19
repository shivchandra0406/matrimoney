from django.db import models

# Create your models here.
from django.db import models
import uuid

from django.contrib.auth.models import AbstractUser
from .option import *
from .manager import UserManager
# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
    

class Registration(AbstractUser):
    username=None
    uid=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    mobilenumber=models.CharField(max_length=12,unique=True)
    gender=models.CharField(max_length=10,choices=(('male','male'),('female','female')))
    
    pic=models.ImageField(upload_to='image')
    #basic details
    dob=models.DateField(null=True,blank=True)
    religion=models.CharField(max_length=200,choices=religion_choices)
    mother_tongue=models.CharField(max_length=100,choices=tongue)

    

    #cast details
    caste=models.CharField(max_length=1000,choices=caste_choices)
    dosh=models.CharField(max_length=100,choices=dosh_choices)
    #personal details
    height=models.CharField(max_length=100)
    marital_status=models.CharField(max_length=100,choices=status_choices)
    any_disability=models.CharField(max_length=100,choices=disability_choices)
    family_status=models.CharField(max_length=100,choices=family_choices)
    family_type=models.CharField(max_length=100,choices=family_type_choices)
    family_value=models.CharField(max_length=100,choices=family_value_choices)
    #profational details
    education=models.CharField(max_length=1000,choices=education_choices)
    employed_in=models.CharField(max_length=100,choices=employee_choices)
    occupation=models.CharField(max_length=100,choices=occupation_choices)
    annual_income=models.CharField(max_length=1000,choices=annual_income_choices)
    work_location=models.CharField(max_length=100,choices=work_choices)
    residing_state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    otp=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    

    USERNAME_FIELD='mobilenumber'
    REQUIRED_FIELDS=[]
    objects=UserManager()





class Package(BaseModel):
    subscribtion_amount=models.IntegerField()
    membership=models.CharField(max_length=30,choices=(('silver','silver'),('gold','gold'),('diamond','diamond')))
    registeruser=models.OneToOneField(Registration,on_delete=models.CASCADE)

class Payment(BaseModel):
    tranc_id=models.CharField(max_length=100)
    payment_mode=models.CharField(max_length=20)
    is_verify=models.BooleanField(default=False)
    register=models.ForeignKey(Registration,on_delete=models.CASCADE)
    pack=models.ForeignKey(Package,on_delete=models.CASCADE)




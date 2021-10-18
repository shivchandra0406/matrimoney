from random import random
from rest_framework import serializers
from .models import *
import random
from .mail import *
class RegistrationSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(required=True)
    last_name=serializers.CharField(required=True)
    email=serializers.EmailField(required=True)
    
    
    class Meta:
        model=Registration
        fields=['uid','password','mobilenumber','religion','gender','mother_tongue','caste','dosh','height','marital_status','any_disability',
        'family_status','family_type','education','annual_income','work_location','residing_state','city','occupation',
        'employed_in','family_value','pic','email','first_name','last_name']
        #read_only_fields=['mobilenumber']

class LoginSerializer(serializers.Serializer):
    mobilenumber=serializers.CharField()
    password=serializers.CharField()
class ChangeSerializer(serializers.Serializer):
    old_password=serializers.CharField(required=True)
    new_password=serializers.CharField(required=True)
    confirm_password=serializers.CharField(required=True)

class UrlValidateSerializer(serializers.Serializer):
    #mobilenumber=serializers.CharField(required=True)
    otp=serializers.CharField(required=True)

class SendOtpSerializer(serializers.ModelSerializer):
    mobilenumber=serializers.CharField(required=True)
    class Meta:
        fileds=['mobilenumber']
        def update(self , instance , validated_data):
        
            instance.mobilenumber = validated_data['mobilenumber']
            otp=random.randint(999,9999)
            instance.otp = otp
            instance.save()
            activate_url = f'{otp}'
            send_otp(instance.email,instance.first_name,activate_url)
            return instance

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Package
        fields='__all__'
        # def create(self,validated_data):
        #     obj=Package.objects.create(
        #         subscribtion_amount=validated_data['subscribtion_amount'],
        #         membership=validated_data['membership'],
        #     )
        #     Package.registeruser=obj



    


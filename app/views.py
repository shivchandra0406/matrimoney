from django.shortcuts import render
from rest_framework import response
from  rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
# Create your views here.

from .mail import *


class RegistrationView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=RegistrationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':'Success',
                    'details':serializer.data
                    })
            return Response({
                    'status':'Failure',
                    'details':serializer.errors
                    })  
        except Exception as e:
            print(e)
            return Response({
                    "status":"Failure",
                    "details":"error"
    
            }) 
import random
class LoginView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=LoginSerializer(data=data)
            if serializer.is_valid():
                mobilenumber=serializer.data['mobilenumber']
                password=serializer.data['password']
                print(password,mobilenumber)
                
               
                if Registration.objects.filter(mobilenumber=mobilenumber).exists():
                   
                    user = authenticate(request,mobilenumber=mobilenumber,password=password)
                    print(user)
                    if user:
                        token,_=Token.objects.get_or_create(user=user)
                        return Response({
                        'status':"Success",
                        'token':str(token),
                        'details':"login successfully"
                        })
                    
                    else:
                        return Response({
                        'status':"Failure",
                        'details':"this mobile number and password are not exist"
                        })    
                return Response({
                    'status':"Failure",
                    'details':"this mobile number is not exist"
                    })

            return Response({
                'status':"Failure",
                'details':serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                    'status':"Failure",
                    'details':"error"
                })


class ChangeNumber(APIView):

    def post(self,request):
        try:
            
            mobilenumber=request.GET.get('mobilenumber')
            data=request.data
            serializer=ChangeSerializer(data=data)
            if serializer.is_valid():
                register=Registration.objects.filter(mobilenumber=mobilenumber).first()
                if register is not None:
                    new_password=serializer.data['new_password']
                    confirm_password=serializer.data['confirm_password'] 
                    old_password=serializer.data['old_password']
                    if(new_password==confirm_password):
                        
                        if(new_password!=old_password):
                            
                            user=authenticate(mobilenumber=mobilenumber,password=old_password)
                            if user is None:
                                return Response({
                                    'status':'Success',
                                    'details':"old password missmatch"
                                })
                            register.set_password(serializer.data['new_password'])
                            register.save()
                            return Response({
                                'status':'Success',
                                'details':'password change successfully'
                            })
                        return Response({
                            'status':'False',
                            'details':'new password and old password are same,please new fill password'

                            })
                    return Response({
                            'status':'False',
                            'details':'new password and confirm passwrod missmatch'

                            })
                    
                return Response({
                    'status':"False",
                    'details':'mobile number is not found'
                })

            
            return Response({
                'status':'False',
                'details':serializer.errors
            })
        except Exception as e:

            print(e)
            return Response({
                'status':'error',
                'error':'somthin went wrong'
            })
    
    



def sendOpt(request):
    try:
        data=request.data
        register=Registration.objects.filter(mobilenumber=data['mobilenumber']).first()
        if register is not None:
            serializer=SendOtpSerializer(register,data=data,partial=True)
            if serializer.is_valid():
               serializer.save()
               mobilenumber=data['mobilenumber']
               response({
                    'status':'Success',
                    'message':f'otp send successfully ,mobile number is {mobilenumber}'
                })
            return Response({
                'status':'Failure',
                'details':serializer.errors
            })
        return Response({
            'status':'Failure',
            'details':"mobilenumber is not found"
        })


    except Exception as e:
        print(e)
        return Response ({
            'status':'error',
            'message':'somthing went wrong'
        })

class VerifyOtp(APIView):
    def post(self,request):
        try:
            mobilenumber=request.GET.get('mobilenumber')
        
            data=request.data
            print(data)
            mseriailizer=UrlValidateSerializer(data=data)
            if mseriailizer.is_valid():
                obj=Registration.objects.filter(mobilenumber=mobilenumber).first()
                if obj is not None:
                    if mseriailizer.data['otp']==obj.otp:
                        return Response({
                            'status':'Success',
                            'details':'otp verify successfully'
                        })
                    return Response({
                        'status':'False',
                        'details':'otp missmatch'
                    })
                return Response({
                    'status':'Failure',
                    'details':'mobilenumber is not found'
                })
            return Response({
                'status':'Failure',
                'details':mseriailizer.errors
            })

        except Exception as e:
            print(e)
            return Response({
                'status':'error',
                'details':'somthing went wrong'
            })
class FindFiveView(APIView):
    def get(self,request):
        try:
            mobilenumber=request.GET.get('mobilenumber')
            print(mobilenumber)
            data=Registration.objects.filter(mobilenumber=mobilenumber).first()
            print(type(data))
            if data is not None:
                print(data)
                gender=data.gender
                if gender=='male':
                    obj=Registration.objects.filter(gender='female')[:5]
                    serializer=RegistrationSerializer(obj,many=True)
                    return Response({
                        'status':"Success",
                        'details':serializer.data
                    })
                else:
                    obj=Registration.objects.filter(gender='male')[:5]
                    serializer=RegistrationSerializer(obj,many=True)
                    return Response({
                        'status':"Success",
                        'details':serializer.data
                    })
            return Response({
                'status':'Failure',
                'details':'something went wrong'
            })
        except Exception as e:
            print('error',e)
            return Response({
                'status':'error',
                'details':'something went wrong'
            })
class  GetFullInfo(APIView):
    def get(self,request):
        try:
            mobilenumber=request.GET.get('mobilenumber')
            print(mobilenumber)
            data=Registration.objects.filter(mobilenumber=mobilenumber).first()

            if data is not None:
                serializer=RegistrationSerializer(data)
                return Response({
                    'status':'Success',
                    'details':serializer.data
                })
            return Response({
                'status':'Failure',
                'details':'somthing went wrong'
            })

        except Exception as e:
            print(e)
            return Response({
                'status':'error',
                'details':'somthing went wrong'
            })

class PackageView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=PackageSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':'Success',
                    'details':serializer.data
                })
            return Response({
                'status':'Failure',
                'details':serializer.errors
            })
        except Exception as e:
            pass
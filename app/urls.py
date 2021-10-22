
from django.urls import path
from .views import *
urlpatterns = [

    path('register/',RegistrationView.as_view()),
    path('loginapp/',LoginView.as_view()),
    path('changeapp/',ChangeNumber.as_view()),
    path('sendotp/<str:mobilenumber>/',send_otp),
    path('otpverify/',VerifyOtp.as_view()),
    path('findfive/',FindFiveView.as_view()),
    path('getprofile/',GetFullInfo.as_view()),
    path('takepackage/',PackageView.as_view())
]
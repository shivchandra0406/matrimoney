
from django.urls import path
from .views import *
urlpatterns = [

    path('register/',RegistrationView.as_view()),
    path('login/',LoginView.as_view()),
    path('changepassword/',ChangeNumber.as_view()),
    path('sendotp/<str:mobilenumber>/',send_otp),
    path('verifyotp/',VerifyOtp.as_view()),
    path('getfiveview/',FindFiveView.as_view()),
    path('getfullinfo/',GetFullInfo.as_view()),
    path('takepackage/',PackageView.as_view())
]
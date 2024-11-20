from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginaccount, name='loginaccount'),
    path('signupaccount/', views.signupaccount, name='signupaccount'),
    path('logout/', views.logoutaccount, name='logoutaccount'),
]

from django.urls import path
from primary import views
urlpatterns = [
    path('',views.index,name='index'),
    path('signUp',views.signUp,name='signUp'),
    path('Login',views.Login,name='Login'),
    path('information',views.information,name='information'),
    path('Donor',views.Donor,name='donor'),
     path('reciever',views.reciever,name='reciever'),
]
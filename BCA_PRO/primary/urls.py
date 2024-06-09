
from django.urls import path
from primary import views
urlpatterns = [
    path('',views.index,name='index'),
    path('user_signup',views.user_signup,name='user_signup'),
    path('user_login',views.user_login,name='user_login'),
    path('information',views.information,name='information'),
    path('Donor',views.Donor,name='donor'),
    path('reciever',views.reciever,name='reciever'),
    path('user_logout',views.user_logout,name='user_logout'),
    # path('profile_img_del/<id>',views.profile_img_del,name='profile_img_del'),
]
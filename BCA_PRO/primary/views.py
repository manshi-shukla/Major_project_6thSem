from primary.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile  # Import the UserProfile model
from django.db import transaction
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,"index.html")
def user_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')

        # Basic validation
        if not all([name, email, phone, address, pincode, password, confirm_password, role]):
            return render(request,'sign_up.html',{'error_msg':'All fields are required.'})
            

        if password != confirm_password:
            return render(request,'sign_up.html',{'error_msg':'Passwords do not match..'})
           

        if User.objects.filter(email=email).exists():
            return render(request,'sign_up.html',{'error_msg':'Email is already registered.'})
            

        try:
            with transaction.atomic():
                # Create the user
                user = User.objects.create_user(username=email, email=email)
                user.first_name = name
                user.set_password(password)
                user.save()

                # Create the user profile
                UserProfile.objects.create(
                    user=user,
                    phone=phone,
                    address=address,
                    pincode=pincode,
                    role=role
                )
            return render(request,'sign_in.html',{'error_msg':'Registration successful!'})
        except ValidationError as e:
            messages.error(request, f"Error: {e.message}")
            return redirect(user_signup)

    return render(request, 'sign_up.html')
# def Login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         role = request.POST.get('role')
#         exist = registered_info.objects.filter(role=role,email=username,password=password).exists()
#         if exist:
#             return render(request,'Donor_Dash.html',{'success_msg':'you have logged in successfully'}) 
#         else:
#             return render(request,'sign_in.html',{'success_msg':'You are not a valid user Please register yourself!'})
#     return render(request,'sign_in.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
       
        if not User.objects.filter(username=email):
            return render(request,'sign_in.html',{'error_msg' : 'Invalid username!'})

       

        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            if UserProfile.objects.get(user = user).role == 'donar':
                login(request, user)
                return render(request,'Donor_Dash.html',{'error_msg':'Login successful!'})   # Redirect to a home page or dashboard
            else:
                login(request,user)
                return render(request,'recipient_Dash.html',{'error_msg':'Login successful!'})
        else:
            return render(request,'sign_in.html',{'error_msg':'Invalid password...'})
            

    return render(request, 'sign_in.html')
def user_logout(request):
    logout(request)
    return render(request,'sign_in.html',{'error_msg':'You have Logged Out!'})


def information(request):
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        message = request.POST.get('message')
        print('success shown')
        # Check if all required fields are present
        if name and contact and message:
            # Create a new record in the 'contact_info' table with the received data
            contact_info.objects.create(name=name, contact=contact, message=message)
            
            # Return a response indicating success, along with rendering the 'information.html' template
            return render(request, 'information.html', {'success_msg': 'Record has been saved!'})
        else:
            # Handle case where required fields are missing
            return render(request, 'information.html', {'error_msg': 'Please fill out all required fields.'})
    return render(request, 'information.html',{'record':UserProfile.objects.all()})

@login_required(login_url='user_login')
def Donor(request):
    return render(request,"Donor_Dash.html")

@login_required(login_url='user_login')
def reciever(request):
    return render(request,"recipient_Dash.html")


     


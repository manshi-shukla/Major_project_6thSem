from django.shortcuts import render
from primary.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")
def signUp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')
        
        # Check if passwords match b
        if password != confirm_password:
            # Handle password mismatch error
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
        # Save form data to the database
        exist = registered_info.objects.filter(role=role,email=email).exists()
        if not exist:
            signup = registered_info(name=name, email=email, phone=phone, address=address, pincode=pincode, password=password,role=role)
            signup.save()
            return render(request,'sign_up.html',{'error':'Your Records has been submitted!'})
        else:
            return render(request,'sign_up.html',{'error':'You are already registered!'})
    return render(request,'sign_up.html')
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        exist = registered_info.objects.filter(role=role,email=username,password=password).exists()
        if exist:
            return render(request,'sign_in.html',{'success_msg':'you have logged in successfully'}) 
        else:
            return render(request,'sign_in.html',{'success_msg':'You are not a valid user Please register yourself!'})
    return render(request,'sign_in.html')

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
    return render(request, 'information.html',{'record':registered_info.objects.all()})
     


from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('donor', 'Donor'),
        ('recipient', 'Recipient'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    pincode = models.CharField(max_length=10, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.user.username

class contact_info(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    message=models.CharField(max_length=200)


    def __str__(self):
        return self.name
    
# nhi aa


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # user_id = models.CharField(max_length=10, unique=True)
#     profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    
#     def __str__(self):
#         return self.user.username


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    items = models.CharField(max_length=255)
    shelf_life = models.IntegerField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return f'{self.user.username} - {self.date}'

class DonationOption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_items = models.CharField(max_length=255)
    shelf_life = models.IntegerField()
    number_of_food = models.IntegerField()
    date_donated = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.food_items}'

class Feedback(models.Model):
    donation = models.ForeignKey(DonationOption, on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=255)
    feedback = models.TextField()
    date_given = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.recipient_name} - {self.date_given}'

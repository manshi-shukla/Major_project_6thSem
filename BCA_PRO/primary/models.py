from django.db import models

# Create your models here.
class registered_info(models.Model):
    ROLE_CHOICES = [
        ('donor', 'Donor'),
        ('recipient', 'Recipient'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    pincode = models.CharField(max_length=6)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class contact_info(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    message=models.CharField(max_length=200)


    def __str__(self):
        return self.name

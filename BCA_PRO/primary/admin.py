from django.contrib import admin
from primary.models import *

# Register your models here.


class register_info(admin.ModelAdmin):
    list_display = ['id','name','email','address','phone','role','pincode']
admin.site.register(registered_info,register_info)

class contacts_info(admin.ModelAdmin):
    list_display = ['name','contact','message']
admin.site.register(contact_info,contacts_info)
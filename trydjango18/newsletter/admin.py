from django.contrib import admin
from .models import SignUp
# Register your models here.
class SignAdmin(admin.ModelAdmin):
    list_display = ('email','full_name','timestamp','updated')
admin.site.register(SignUp,SignAdmin)
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=40)
    profile = models.ImageField(null=True,blank=True)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.full_name
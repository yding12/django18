from django import forms
from .models import SignUp

class AddPosts(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email','full_name','profile']


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=120)
    email = forms.EmailField()
    message =forms.CharField(widget=forms.Textarea)


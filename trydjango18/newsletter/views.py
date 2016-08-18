from django.shortcuts import render
from .forms import AddPosts, ContactForm
from .models import SignUp
# Create your views here.
def home(request):
    title = 'Welcome '
    # if request.method == 'POST':
    forms = AddPosts(request.POST or None, request.FILES or None)
    if forms.is_valid():
        instance = forms.save(commit=False)
        if not instance.full_name:
            instance.full_name = 'Han'
        instance.save()
    context = {
        "title":title,
        "forms": forms,
    }
    if request.user.is_authenticated() or request.user.is_staff:
        queryset = SignUp.objects.all()
        for instance in queryset:
            print(instance)
        context = {
            "queryset":queryset,
        }

    return render(request,'home.html',context)


def contact(request):
    subj = ""
    email = ""
    message = ""

    forms = ContactForm(request.POST or None)
    context = {
        "forms": forms,

    }
    if forms.is_valid():
        subj = forms.cleaned_data['subject']
        email = forms.cleaned_data['email']
        message = forms.cleaned_data['message']
        context = {

            "subject": subj,
            "email": email,
            "message": message,

        }
    return render(request, 'nav.html', context)


def video(request):
    return render(request,'video.html',{})

def story(request):
    return render(request,'story.html',{})

def picture(request):
    return render(request,'picture.html',{})

def blog(request):
    return render(request,'blog.html',{})

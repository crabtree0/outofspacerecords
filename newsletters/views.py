from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterUser
from .forms import NewsletterUserSignupForm

def newsletter_signup(request):
    form = NewsletterUserSignupForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Your email already exists',
                             'alert alert-warning alert-dismissible')
        else:
            instance.save()
            messages.success(request, 'Your email has been submitted', 'alert alert-success alert-dismissible')
            return redirect('home')


    form = NewsletterUserSignupForm()
    template = "newsletters/signup.html"
    return render(request, template, {'form':form})

def newsletter_unsubscribe(request):
    form = NewsletterUserSignupForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'Your email has been removed', 'alert alert-success alert-dismissible')
        else:
            messages.warning(request, 'Your email is not in the database', 'alert alert-warning alert-dismissible')


    template = "newsletters/unsubscribe.html"
    return render(request, template, {'form': NewsletterUserSignupForm()})




# Create your views here.

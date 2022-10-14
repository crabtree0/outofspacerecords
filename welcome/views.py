import json
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Contact

def home(request):
    return render(request, 'welcome/home.html', {'form': ContactForm})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name' : form.cleaned_data['first_name'],
                'last_name' : form.cleaned_data['last_name'],
                'email' : form.cleaned_data['email_address'],
                'message' : form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            html = "<div id='email-error' _='on load wait 1s trigger closeModal'>Success</div>"
            try:
                send_mail(subject, message, 'outofspacerecords@yahoo.com', ['outofspacerecords@yahoo.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse(status=204,
                                headers={
                                    'HX-Trigger': json.dumps({"showMessage": "Thank You For Your Enquiry We Will Be In Touch Shortly"})
                                })
    else:
        form = ContactForm()
    return render(request, 'welcome/contact.html', {'form':form, 'successful_submit': True})

def success(request):
    return render(request, 'welcome/messages.html')

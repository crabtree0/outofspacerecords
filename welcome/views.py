import json
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Contact
from .models import User
from django.db.models import Q


def home(request):


    ### Get IP Address ####

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)
    u = User(user=ip)
    print(ip)
    result = User.objects.filter(Q(user__icontains=ip))
    if len(result) == 1:
        print("user exists")
    elif len(result) > 1:
        print("user exists more...")
    else:
        u.save()
        print("user is unique")

    count = User.objects.all().count()
    print("total user is", count)

    return render(request, 'welcome/home.html', {'form': ContactForm, 'count': count})

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
                send_mail(subject, message, 'info@outofspacerecords.com', ['outofspacerecords@yahoo.com'])
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









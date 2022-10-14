from django import forms
from.models import NewsletterUser

class NewsletterUserSignupForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'placeholder': 'Email'
        }
    ))
    class Meta:
        model = NewsletterUser
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')

            return email




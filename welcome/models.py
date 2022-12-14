from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=150)
    message = models.TextField(max_length=2000)

class User(models.Model):
    user = models.TextField(default=None)
    def __str__(self):
        return self.user



# cms_app/models.py
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model








def validate_numeric(value):
    if not value.isdigit():
        raise ValidationError('Phone number must contain only numeric characters.')


class Admin(AbstractUser):
    phone = models.CharField(max_length=10, blank=True, null=True, validators=[validate_numeric])
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{1,6}$', message='Please enter a valid numeric pincode.')])

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'cms_app'

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='cms_user_permissions'  # Change this to a unique name
    )
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='cms_user_groups'  
    )


class Author(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    summary = models.TextField(max_length=100, blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title
   

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'cms_app'

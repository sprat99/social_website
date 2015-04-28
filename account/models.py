from django.db import models
from django.forms import ModelForm

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=18)

    def __unicode__(self):
        return self.email

class Info(models.Model):
    email = models.OneToOneField(User)
    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICES = (
                      (MALE,'Male'), 
                      (FEMALE,'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=MALE)
    
    pic = models.ImageField(upload_to='img/account_pic/')
    profile = models.TextField()

class UserForm(ModelForm):
    class Meta:
        model = User
        field = ['email', 'password']

class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ['email', 'gender', 'pic', 'profile']

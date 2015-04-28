from django.db import models
from django.forms import ModelForm

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=18)
    friends = models.ManyToManyField('self', null=True, blank=True)
#     friends = models.ManyToManyField('self', through='Friendship', null=True, blank=True)
    def __unicode__(self):
        return self.email

# class Friendship(models.Model):
#     from_user = models.ForeignKey(User, related_name="from_user")
#     to_user = models.ForeignKey(User, related_name="to_user")
#     friend_type = models.CharField(max_length=255)
#     friend_rated = models.FloatField()

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
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    age = models.IntegerField(default=0)
    major = models.CharField(max_length=100, blank=True)
    profile = models.TextField(blank=True)
    def __unicode__(self):
        return self.email

class UserForm(ModelForm):
    class Meta:
        model = User
        field = ['email', 'password']

class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ['email', 'gender', 'age', 'phone', 'major', 'address', 'pic', 'profile']

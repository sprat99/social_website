from django.db import models
from django.forms import ModelForm
from account.models import User, Info
# Create your models here.
    
class Education(models.Model):
    user = models.OneToOneField(User)
    BACHELOR = 'Bachelor'
    MASTER = 'master'
    DOCTOR = 'doctor'
    
    DEGREE_CHOICES = (
                      (BACHELOR, 'Bachelor'),
                      (MASTER, 'master'),
                      (DOCTOR, 'doctor'),
                      )
    
    degree = models.CharField(max_length=8, choices=DEGREE_CHOICES, default=BACHELOR, blank=True)
    school = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.user.email
    

class Experience(models.Model):
    user = models.OneToOneField(User)
    activity = models.TextField(blank=True)
    internship = models.TextField(blank=True)
    awards = models.TextField(blank=True)
    association = models.TextField(blank=True)
    other = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.user.email

# class Resume(models.Model):
#     user = models.OneToOneField(User)
#     info = models.OneToOneField(Info)
#     education = models.OneToOneField(Education)
#     experience = models.OneToOneField(Experience)
#     
#     def __unicode__(self):
#         return self.user.email

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['user', 'degree', 'school', 'department']

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['user', 'activity', 'internship', 'awards', 'association', 'other']

# class ResumeForm(ModelForm):
#     class Meta:
#         model = Resume
#         fields = ['user', 'info', 'education', 'experience']

from django.contrib import admin
from models import Status, Resume
# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'message', 'picture', 'timestamp']

class ResumeAdmin(admin.ModelAdmin):
    list_display = ['user' ]

admin.site.register(Status, StatusAdmin)
admin.site.register(Resume, ResumeAdmin)
from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User
from app.models import ExtendUser



# Create your models here.
class Log(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='logs')
    is_correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"
    
class Attendance(models.Model):
    employee_key = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, blank=True, null=True)
    employee_name = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    timein = models.TimeField(null=False, default='00:00:00') # accepts %H:%M:%S
    timeout = models.TimeField(null=False, default='00:00:00') # accepts %H:%M:%S
    total_hours = models.IntegerField(null=False, default='0')
    overtime = models.IntegerField(null=False, default='0')
    


    def __str__(self) -> str:
        return f"{self.employee_name}"



    
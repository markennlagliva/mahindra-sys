from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MaxLengthValidator, RegexValidator

from django.contrib.auth.models import User
# Create your models here.


class ExtendUser(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
    userid = models.IntegerField(validators=[MaxValueValidator(300000)], null=True)
    employee_mahindra = models.CharField(max_length=100, null=True)
    age = models.IntegerField(validators=[MaxValueValidator(65)], null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=50, null=True)
    department = models.CharField(max_length=50, null=True)
    occupation = models.CharField(max_length=50, null=True)
    fullname = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)

    # photo = models.ImageField(blank=True, upload_to='photos')

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f"{self.user}"
    


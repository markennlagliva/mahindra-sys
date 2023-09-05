from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MaxLengthValidator, RegexValidator

# Create your models here.

# created_at = models.DateTimeField(auto_now_add=True)

class Registered(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    userId = models.IntegerField(validators=[MaxValueValidator(300000)])
    firstname_and_middlename = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MaxValueValidator(65)])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    password = models.CharField(max_length=128,
    validators= [
        MinLengthValidator(limit_value=8, message="Password must be at least 8 characters long."),
        MaxLengthValidator(limit_value=128, message="Password cannot exceed 128 characters."),
        RegexValidator(
            regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).*$', 
            message="Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character."
        ),
    ]                          
)   
    confirmpass = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.firstname_and_middlename
    
    

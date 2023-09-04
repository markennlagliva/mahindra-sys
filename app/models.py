from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MaxLengthValidator, RegexValidator

# Create your models here.
class Admin(models.Model):
    userId = models.IntegerField(validators=[MaxValueValidator(300000)])
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
    # def __str__(self):
    #     return str(self.userId)
    
class Employee(models.Model):
    userId = models.IntegerField(validators=[MaxValueValidator(7)])
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

# created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import AbstractUser

class LoginPageSettings(models.Model):
    background_image = models.ImageField(upload_to='loginPage/')
    
class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    contact_number = models.CharField(max_length=11, null=True, blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        related_query_name='user',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        related_query_name='user',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
    
class bookstore(models.Model):
    book_id = models.AutoField
    book_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=1000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='BookStore/images', default="")
    step1_image = models.ImageField(upload_to='BookStore/step1', default="")
    step2_image = models.ImageField(upload_to='BookStore/step2', default="")
    step3_image = models.ImageField(upload_to='BookStore/step3', default="")
    step4_image = models.ImageField(upload_to='BookStore/step4', default="")
    step5_image = models.ImageField(upload_to='BookStore/step5', default="")
    step6_image = models.ImageField(upload_to='BookStore/step6', default="")

    def __str__(self):
        return self.routine_name
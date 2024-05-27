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
    
class BookStore(models.Model):
    book_id = models.AutoField(primary_key=True)
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
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.book_name
    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
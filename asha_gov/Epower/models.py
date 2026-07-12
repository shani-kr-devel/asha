from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Epower(models.Model):
    PD = [
        ('Product 1', 'Product 1'),
        ('Product 2', 'Product 2'), 
        ('Product 3', 'Product 3')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date = models.DateField(default=timezone.now)
    message = models.TextField()
    def __str__(self):
        return self.name    
    type= models.CharField(max_length=100, choices=PD)
    price= models.DecimalField(max_digits=10, decimal_places=2,default=1000000.00)

    def get_absolute_url(self):
        return reverse('epower_detail', kwargs={'pk': self.pk})
    
#one to many relationship with user
class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='user_reviews')
    epower = models.ForeignKey(Epower, on_delete=models.CASCADE, related_name='epower_reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reviews{self.user.username} - {self.epower.name} - {self.rating}"
    

# many to many relationship with user
class shope(models.Model):
    user = models.ManyToManyField(User, related_name='user_shope')
    epower = models.ManyToManyField(Epower, related_name='epower_shope')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Shope{self.user.username} - {self.epower.name}"
    
# one to one relationship with user

class  UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"Profile {self.user.username} - {self.address}"






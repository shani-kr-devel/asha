from django.db import models
from django.urls import reverse
from django.utils import timezone
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
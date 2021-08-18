from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reviews(models.Model):
    review=models.CharField(max_length=100,default="none")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CHOICES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    rating=models.CharField(max_length=3, choices=CHOICES, default='2')

    def __str__(self):
        return self.review[:10] + '...'
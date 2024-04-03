from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Amount(models.Model):
    user_amount = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    main_amount = models.IntegerField(max_length=20)

    def __str__(self):
        return str(self.user_amount)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    random_number = models.IntegerField(max_length=10)

    def __str__(self):
        return str(self.user)
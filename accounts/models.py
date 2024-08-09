from django.db import models
from django.contrib.auth.models import User

# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class BankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active= models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username} - {self.account_number}"
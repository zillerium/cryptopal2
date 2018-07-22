from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    account_email = models.CharField(max_length=200)
    #account_value = models.FloatField(default=0)
    amount_available = models.FloatField(default=0)

    def __str__(self):
        return self.userID.username


class Transaction(models.Model):
    accountID = models.ForeignKey(Account, on_delete=models.CASCADE)
    quantity_moved = models.IntegerField(default=0)
    time = models.DateTimeField()

    def __str__(self):
        time_string = str(self.time)
        return time_string

class 

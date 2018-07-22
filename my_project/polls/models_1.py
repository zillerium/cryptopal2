from django.db import models

class Email(models.Model):
    email_address = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')

    def __str__(self):
    	return self.email_address

#class Choice(models.Model):
    #question = models.ForeignKey(Email, on_delete=models.CASCADE)
    #choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

class Username(models.Model):
    name = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    def __str__(self):
    	return self.name

class Signature(models.Model):
	sign = models.CharField(max_length=200)
	def __str__(self):
		return self.sign



#####################################################

from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    account_value = models.FloatField(default=0)
    amount_available = models.FloatField(default=0)

    def __str__(self):
        return self.userID.username


class Transaction(models.Model):
    accountID = models.ForeignKey(Account, on_delete=models.CASCADE)
    #comodity = models.CharField(max_length=5)
    quantity_moved = models.IntegerField(default=0)
    current_price = models.FloatField(default=0)
    #transaction_type = models.BooleanField()
    time = models.DateTimeField()

    def __str__(self):
        time_string = str(self.time)
        return time_string

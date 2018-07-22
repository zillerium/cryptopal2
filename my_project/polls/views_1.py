from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):

	if request.method == 'POST':
		#validate username
		#if username.lower() exists, check balance
		#
		#send amount
		# check if send amount is < balance
		#	if true, balance - send_amount
		#	else return "insufficient funds"
		#record target email
		#record  of sender name

		validate = request.POST['validate']

    return HttpResponse("Testing.")


def check_balance(request):
	if request.method == 'POST':

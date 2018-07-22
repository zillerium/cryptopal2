from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound
import json
#from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
	if request.method == 'POST':
		data = request.POST
		#content = json.loads(data)
		name = data['name']
		email = data['email']
		friend_email = data['friend_email']
		amount = data['amount']
		currency = data['currency']
		if name and email and friend_email and amount:
			return HttpResponse(email)
		else:
			return HttpResponse("require details!")
	else:
		return HttpResponse("Not.")
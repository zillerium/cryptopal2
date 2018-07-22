from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect


#def index(request):
#    return HttpResponse("Testing.")

def index(request):
    """Login page"""

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            #return HttpResponse("Success") 
            return render(request,'login/no_success.html',{'error':error})
        else:
        	return HttpResponse("NO Success")
            #error = " Sorry! Email and Password didn't match, Please try again ! "
            #return render(request, 'login/login.html',{'error':error})
    else:   # First landing on page
        return HttpResponse("NO Success_1")
        #return render(request, 'login/login.html')

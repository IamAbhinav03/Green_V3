from django.http.response import HttpResponse, HttpResponseRedirect
from account.models import Account
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def home(request):
	return render(request, 'Home.html')

@login_required()
def empty(request):
	return render(request, 'Empty-Trash.html')

# @login_required()
# def collection(request):
# 	if request.user.is_staff:
# 		return HttpResponseRedirect('/admin/accounts/consumer/')
# 	else:
# 		return HttpResponse("You don't have access to this page")

@login_required()
def profile(request):
	user = request.user
	username = user.username
	con = Account.objects.get(username=username)
	points = con.points
	return render(request, 'Profile.html', {'username': username, 'points': points})


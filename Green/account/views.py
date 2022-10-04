from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
from .forms import NewUserForm, NewStaffForm
from .models import Account
from django.http import HttpResponse

# Create your views here.
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("/")
		print("Not valid")
		messages.error(request, "Unsuccessful registration. Invalid information")
	form = NewUserForm(auto_id=False)
	return render(request, template_name="registration/register.html", context={"form": form})

def staff_register_request(request):
	if request.method == "POST":
		form = NewStaffForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("/")
		print("Not valid")
		messages.error(request, "Unsuccessful registration. Invalid information")
	form = NewStaffForm(auto_id=False)
	return render(request, template_name="registration/register.html", context={"form": form})


def login_request(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			redirect('/accounts/test')
		else:
			messages.error(request, 'Invalid Credentials Provided')
	else:
		render(request, 'login.html')


@login_required()
def logout_request(request):
	logout(request)

@login_required()
def test_request(request):
	text="""<h1>Welcom to my App</h1>"""
	return HttpResponse(text)

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserRegisterForm, LoginForm
from .models import User
from .functions import LogIn
from braces.views import LoginRequiredMixin
from django.views.generic import  TemplateView

class Home(LoginRequiredMixin, TemplateView):
	login_url ='/'
	template_name = 'users/home.html'


def userlogin(request):
	if request.method == "POST":
		if 'register_form' in request.POST:
			user_register = UserRegisterForm(request.POST)
			if user_register.is_valid():
				User.objects.create_user(username = user_register.cleaned_data['username'],
				 email = user_register.cleaned_data['email'], 
				 password = user_register.cleaned_data['password'])
				LogIn(request, user_register.cleaned_data['username'],
						user_register.cleaned_data['password'])
				return redirect('/')
		if 'login_form' in request.POST:
			login_form = LoginForm(request.POST)
			if login_form.is_valid():
				LogIn(request, login_form.cleaned_data['username'],
						login_form.cleaned_data['password'])
				return redirect('/home')
		else:
			user_register = UserRegisterForm()
			login_form = LoginForm()
			return redirect('/')
	else:
			user_register = UserRegisterForm()
			login_form = LoginForm()
			
	return render(request, 'users/login.html', 
				{'login_form' : login_form})


def LogOut(request):
	logout(request)
	return redirect('/')
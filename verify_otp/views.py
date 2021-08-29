from typing import Generic
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.
# @csrf_protect 
# class RegisterUserView(Generic.createview):
def RegisterView(request):
  first_name=""
  last_name=""
  # username=""
  RegisterView.user_email=""
  password=""
  password2=""
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    RegisterView.user_email = email

    print(RegisterView.user_email)

    if password == password2:
      user = User.objects.create(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
      user.save()
      return redirect('verify')
  else:
    return render(request, 'registration/register.html')

def login(request):
  pass

def logout(request):
  pass

def verify(request):
  print(RegisterView.user_email)  
  
  return render(request, 'registration/verify.html')

from typing import Generic
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.core.mail import send_mail
from verification.settings import EMAIL_HOST_USER
import string
from random import choice

# Create your views here.
# @csrf_protect 
# class RegisterUserView(Generic.createview):
def RegisterView(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    RegisterView.user_first_name = first_name
    RegisterView.user_last_name = last_name
    RegisterView.user_username = username
    RegisterView.user_email = email
    RegisterView.user_password = password
    RegisterView.user_password2 = password2


    print("register FUnction")

    # print(RegisterView.user_email)

    if password == password2:
      # user = User.objects.create(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
      # user.save()
      return redirect('verify')
  else:
    return render(request, 'registration/register.html')

def login(request):
  pass

def logout(request):
  pass

def verify(request):
  print("Verify Function")
  # print(RegisterView.user_email)  
  # print(RegisterView.user_first_name)
  # print(RegisterView.user_last_name)
  # print(RegisterView.user_username)
  # print(RegisterView.user_password)
  
  # print(EMAIL_HOST_USER)

  chars = string.digits
  random_otp =  ''.join(choice(chars) for _ in range(6))
  print("OTP: ", random_otp)
  print("RANDOM_OTP var type before: ",type(random_otp))
  random_otp = int(random_otp)
  print("RANDOM_OTP var type after: ",type(random_otp))
  # send_mail (
  #     'OTP FOR ACCOUNT VERIFICATION',
  #     'OPT:'+ random_otp,
  #     EMAIL_HOST_USER,
  #     [RegisterView.user_email],
  #     fail_silently=False,
  #   )

  
  if request.method == 'POST':
    print("Inside IF")
    otp = request.POST['otp']
    print("opt var type",type(otp))

    otp = int(otp)
    print("opt var type after conversion",type(otp))

    if otp == random_otp:
      print("OTP ENTERED IS: ", otp)
      # user = User.objects.create(username = RegisterView.user_username, password = RegisterView.user_password, email = RegisterView.user_email, first_name = RegisterView.user_first_name, last_name = RegisterView.user_last_name)
      # user.save()
      return redirect('login')
    else:
      messages.Error(request,'invalid otp')
      return redirect('register')

  return render(request, 'registration/verify.html')

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login , get_user_model

# Create your views here.

User = get_user_model()

def login_view(request,*args,**kwargs):
    username = request.POST.get('username') or None
    password = request.POST.get('password') or None
    if all([username,password]):
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')


    return render(request,'auth/login.html')
    
    
def register_view(request,*args,**kwargs):
    username = request.POST.get('username') or None
    password = request.POST.get('password') or None
    
    try:    
        user  = User.objects.create_user(username=username,password=password)
    except :
        pass

    return render(request,'auth/register.html')
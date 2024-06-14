from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,get_user_model
from .forms import loginform
from .forms import registrationform
from django.http import HttpResponse



def home(request):
    return HttpResponse("hello")


def login_view(request):
    if request.method == "POST":
        form=loginform(request.POST)

        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(request,email=email,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                pass

    else:
        form = loginform()
        return render(request, 'login.html',{'form':form})
    

def registration_view(request):
    if request.method == "POST":
        form= registrationform(request.POST)
        if form.is_valid():
            User=get_user_model()
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            mobile=form.cleaned_data['mobile']
            password=form.cleaned_data['password']
            User=User.objects.create_user(email=email,password=password,name=name,mobile=mobile)
            # user.save()
            return redirect('login')
        else:
            pass
        
    else:
        form=registrationform()
        return render(request, 'registration.html',{'form':form})

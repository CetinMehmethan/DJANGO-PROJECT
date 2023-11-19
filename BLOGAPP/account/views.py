from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginUserForm ,NewUserForm ,ChangePasswordUserForm
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def user_login(request):
     if request.user.is_authenticated and "next" in request.GET:
         return render(request,"user_login.html",{'error':"Yetkiniz Yok."})

     if request.method == "POST":
        form = LoginUserForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                messages.add_message(request, messages.SUCCESS, "GİRİŞ BAŞARILI")
                next_url= request.GET.get("next",None)
                if next_url is None:
                   return redirect("index")
                else:
                   return redirect(next_url)
            else:
                return render(request, "user_login.html", {"form":form})
        else:
             return render(request,"user_login.html",{"form":form})
     else:
      form = LoginUserForm
      return render(request,'user_login.html',{"form":form})




def change_password(request):
    if request.method == "POST":
        form = ChangePasswordUserForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Parola Güncellendi")
            return redirect("change_password")
        else:
            return render(request, 'change-password.html', {"form": form})

    form = ChangePasswordUserForm(request.user)
    return render(request, 'change-password.html', {"form": form})

def user_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
         form.save()

         username = form.cleaned_data["username"]
         password = form.cleaned_data["password1"]

         user = authenticate(request,username=username,password=password)
         login(request,user)
         return redirect('index')
        else:
         return render(request, 'user_register.html', {'form': form})

    else:
     form = NewUserForm()
     return render(request,'user_register.html',{'form':form})


def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "ÇIKIŞ BAŞARILI")
    return redirect("index")




from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout
from .forms import UserLoginForm , UserRegisterForm
from django.views import View

# Create your views here.

class LoginView(View):
    def get(self,request):
        form = UserLoginForm()
        return render(request , "accounts/form.html" , {
        "form" : form,
        "title" : "Login" ,})

    def post(self,request):
        form = UserLoginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username , password = password)
            login(request , user)
            return redirect("/")
        return render(request , "accounts/form.html" ,
                {
                "form" : form,
                "title" : "Login" ,})


class RegisterView(View):
    def get(self,request):
        form = UserRegisterForm()
        return render(request , "accounts/form.html",{
            "title" : "Register",
            "form" : form,
            })

    def post(self,request):
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data.get("password")
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username , password=password)
            login(request , new_user)
            return redirect("/accounts/login")

        return render(request , "accounts/form.html",{
            "title" : "Register",
            "form" : form,
            })


class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect("/")


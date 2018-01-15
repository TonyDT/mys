from django.shortcuts import render,redirect
from . import models
# Create your views here.
from django import  forms
from . import  forms


def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login.html', locals())

def register(request):
    return render(request,'register.html')

def logout(request):
    #redirect用户Logout后页面重新定向到index首页
    return redirect("/index/")

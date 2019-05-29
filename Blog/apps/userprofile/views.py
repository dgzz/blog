from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from .forms import UserLoginForm,UserRegisterForm
# Create your views here.

# 用户登录
def user_login(request):
    if request.method == 'POST':
        # 实例化表单
        user_login_form = UserLoginForm(data=request.POST)
        # 验证表单的数据类型是否错误
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            # 认证，验证账号密码是否正确
            user = authenticate(username = data['username'],password = data['password'])
            if user:
                # 登录，将信息写入session
                login(request,user)
                return redirect("article:article_list")
            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")

    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")

# 用户登出
def user_logout(request):
    logout(request)
    return redirect('article:article_list')

# 用户注册
def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # 设置密码
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # 保存好数据以后立即登录并返回博客列表界面
            login(request,new_user)
            return redirect('article:article_list')
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = {'form':user_register_form}
        return render(request,'userprofile/register.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")

    pass
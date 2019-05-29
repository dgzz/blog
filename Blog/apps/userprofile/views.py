from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from .forms import UserLoginForm
# Create your views here.

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

def user_logout(request):
    logout(request)
    return redirect('article:article_list')

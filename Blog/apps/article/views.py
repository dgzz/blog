from django.shortcuts import render,redirect
import markdown

from django.conf import settings
from django_redis import get_redis_connection
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework_jwt.serializers import User

from .models import ArticlePost
from article.serializers import ArticleListSerialzier, ArticleDetailSerialzier

from .forms import ArticlePostForm
# Create your views here.

# 文章列表页
class ArticleListView(APIView):
    def get(self, request, *args, **kwargs):
        articles = ArticlePost.objects.all()
        serializer = ArticleListSerialzier(articles, many=True)
        context = {'articles': serializer.data}
        return render(request, 'article/list.html', context)


class ArticleDetailView(APIView):
    def get(self, request, id):
        # 取出所有博客文章
        article = ArticlePost.objects.get(id=id)

        # 将markdown语法渲染成html样式
        article.body = markdown.markdown(article.body,
                                         extensions=[
                                             # 包含 缩写、表格等常用扩展
                                             'markdown.extensions.extra',
                                             # 语法高亮扩展
                                             'markdown.extensions.codehilite',
                                         ])
        # 需要传递给模板（templates）的对象
        serializer = ArticleDetailSerialzier(article)
        context = {'article': serializer.data}
        # render函数：载入模板，并返回context对象
        return render(request, 'article/detail.html', context)

# 发布新文章
class ArticleLCreateView(APIView):

    def get(self, request, *args, **kwargs):
        return render(request, 'article/create.html')

    def post(self, request, *args, **kwargs):
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            new_article.author = User.objects.get(id=1)
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("article:article_list")
        # 如果数据不合法，返回错误信息
        else:
            return Response("表单内容有误，请重新填写。")

# 删除文章
def article_delete(request,id):
    # 根据 id 获取需要删除的文章
    article = ArticlePost.objects.get(id=id)
    # 调用.delete()方法删除文章
    article.delete()
    # 完成删除后返回文章列表
    return redirect("article:article_list")


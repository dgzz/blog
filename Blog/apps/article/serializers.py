from rest_framework import serializers
from article.models import ArticlePost

from .forms import ArticlePostForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

class ArticleListSerialzier(serializers.ModelSerializer):

    class Meta:
        model = ArticlePost
        fields = '__all__'


class ArticleDetailSerialzier(serializers.ModelSerializer):

    class Meta:
        model = ArticlePost
        fields = '__all__'

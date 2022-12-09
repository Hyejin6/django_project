from django.shortcuts import render
from django.views.generic import TemplateView # 템플릿 뷰 상속

# Create your views here.

class HomeView(TemplateView) :
    template_name = 'home/home.html'

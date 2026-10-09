from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def home(request):
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'news/home.html', {'articles': articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'news/article_detail.html', {'article': article})

def category_articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = category.articles.all().order_by('-published_date')
    return render(request, 'news/category_articles.html', {
        'category': category,
        'articles': articles
    })
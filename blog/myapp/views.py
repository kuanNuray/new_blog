from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from myapp.models import *
from datetime import datetime
from myapp.models import Categories

# Create your views here.
# menu=["Добавить","О нас","Логин","Регистрация"]

menu=[{'title':'About us', 'url_name':'about'}]
def category(request, number):
    return HttpResponse(f"Вы на странице категории {number}")

def posts(request):
    # Получаем все посты из базы данных
    all_posts = Posts.objects.all()
    return render(request, 'posts.html', {'posts': all_posts})

def arhiv (request):
    return HttpResponse("Вы на странице Архивов")

def comments (request):
    return HttpResponse("Вы на странице коментариев")

def tegi (request, sluff):
    return HttpResponse(f"Вы на странице тегов {sluff}")

def index(request):
    # Posts.objects.all()
    all_posts = Posts.objects.all()
    category = Categories.objects.all()
    return render(request, 'home.html', {'menu': menu, 'posts': all_posts, 'category': category})


def archive(request, year):
    year=int(year)
    if year>2024:
        raise Http404('Ошибка')
    
    return HttpResponse(f'Архив {year} года')

def error(request,exception):
    return HttpResponseBadRequest('вы ошиблись')


def posts_by_date(request):
    specific_date = datetime(2024, 6, 4)
    posts = Posts.objects.filter(created_at__date=specific_date)
    return render(request, 'posts_by_date.html', {'posts': posts})


def about_us(request):
    return render(request, 'about.html')


def register(request):
    # Posts.objects.all()
    return render(request, 'register.html')


def posts_by_category(request, categories_id):
    category = get_object_or_404(Categories, id=categories_id)
    posts = Posts.objects.filter(categotia=category)
    return render(request, 'posts_by_category.html', {'category': category, 'posts': posts})

# def show_post(request, post_id):
#     all_posts = Posts.objects.all()
#     category = Categories.objects.filter(post_id=post_id)
#     return render(request, 'home.html', {'menu': menu, 'posts': all_posts, 'category': category})


def post_detail(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    category=Categories.objects.all()
    return render(request, 'post_detail.html', {
        'title':post.title,
        'post': post,
        'category':category})
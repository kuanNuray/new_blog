"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories', view=category),
    path('categories/<int:number>', view=category),
    path('posts', view=posts, name='all_posts'),
    path('posts/<str:postr>', view=posts),
    path('tegi/<slug:sluff>', view=tegi),
    path('arhiv', view=arhiv),
    path('comments', view=comments),
    re_path(r'^archive/(?P<year>[0-9]{4})/', view=archive),
    path('', view=index, name='home'),
    path('posts/date/04-06-2024', view=posts_by_date, name='posts_by_date'),
    path('about', view=about_us, name='about_us'),
    path('about_us/', about_us, name='about'),
    path('register/', register, name='register'),
    path('posts/', posts, name='posts'),
    path('category/<int:categories_id>/', posts_by_category, name='posts_by_category'),
     path('post/<int:post_id>/', post_detail, name='post_detail'),
]

handler404=error
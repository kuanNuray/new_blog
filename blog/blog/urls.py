from django.contrib import admin
from django.urls import path, re_path, include
from myapp.views import *
from blog import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
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

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
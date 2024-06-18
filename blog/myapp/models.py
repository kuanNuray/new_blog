from django.db import models
from django.shortcuts import reverse



class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=2000)
    is_published = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categotia=models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)
    slug=models.SlugField(max_length=255, db_index=True, unique=True,verbose_name='ссылка')
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_id': self.pk})




class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter
from django.utils.html import format_html

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status__in=[True])        

class Category(models.Model):
    parent =models.ForeignKey('self',default = None, null = True, blank = True, on_delete = models.SET_NULL, related_name = 'children', verbose_name = 'زیر دسته')
    title = models.CharField('عنوان دسته بندی',max_length=100)
    slug = models.SlugField('آدرس دسته بندی',max_length=100,unique=True)
    status = models.BooleanField('آیا نمایش داده شود',default = True)
    position = models.IntegerField('پوزیشن')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی' 
        verbose_name_plural = 'دسته بندی ها'  
        ordering = ['parent__id','position'] 
    objects = CategoryManager()      

class Article(models.Model):
    STATUS_CHOICES =(
        ('d','پیش نویس'),
        ('p','منتشر شده'),
    )
    title = models.CharField('عنوان',max_length=100)
    slug = models.SlugField('اسلاگ',max_length=100,unique=True)
    category = models.ManyToManyField(Category, verbose_name = 'دسته بندی',related_name="articals")
    discription = models.TextField('توضیحات')
    thumnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField('وضعیت', max_length=1,choices=STATUS_CHOICES)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'مقاله' 
        verbose_name_plural = 'مقالات'   
        ordering = ['created'] 
    def jpublish(self):
        return jalali_converter(self.publish)    
    jpublish.short_description = "زمان انتشار"    

    def thumbnail_tag(self):
        return format_html("<img width=90 style='border-radius:5px' src='{}'>".format(self.thumnail.url))
    thumbnail_tag.short_description = "تصویر"     
    objects = ArticleManager()    
    


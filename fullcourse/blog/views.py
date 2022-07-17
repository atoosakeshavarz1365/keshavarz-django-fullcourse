from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Article, Category
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView


# --- create view without create Html File by HttpResponse
# def home(request):
#     return HttpResponse('hello')

# --- create view with json response with JsonResponse
# def api(request):
#     data ={
#         "1":{"id":1,"title":'python'},
#         "2":{"id":2,"title":'java'},
#         "3":{"id":3,"title":'c++'}
#     }
#     return JsonResponse(data)

# def home(request, page=1):
#     #  --- use Manager published
#     articles_list = Article.objects.published()
#     paginator = Paginator(articles_list, 2)
#     articles = paginator.get_page(page)
#     context ={
#         # "articles":Article.objects.filter(status="p").order_by("-publish"),
#         "articles":articles,
#     }
#     return render(request,'blog/home.html',context)

#  --- write home method with Class Base View
class ArticleList(ListView):
    # --- return all Articles
    # model = Article
    queryset = Article.objects.published()
    template_name = 'blog/article_list.html'
    paginate_by = 2



# def detail(request,slug):   
#     context ={
#     # "article":get_object_or_404(Article,slug=slug,status="p")
#     #  --- use Manager published
#     "article":get_object_or_404(Article.objects.published(),slug=slug)
#     }
#     return render(request,'blog/detail.html',context)

#  --- write detail with Class Base View
class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(),slug=slug)

# def category(request,slug, page=1):
#     category = get_object_or_404(Category,slug=slug,status__in=[True])
#     articles_list = category.articals.published()
#     paginator = Paginator(articles_list, 2)
#     articles = paginator.get_page(page)
#     context ={
#     "category":category,
#     "articles":articles,
#     }
#     return render(request,'blog/category.html',context)

# --- category with Class Base View
class CategoryList(ListView):
    paginate_by =2
    template_name = 'blog/category_list.html'
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(),slug=slug)
        return category.articals.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = category 
        return context

class AuthorList(ListView):
    paginate_by =2
    template_name = 'blog/author_list.html'
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User,username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = author
        return context

        

    

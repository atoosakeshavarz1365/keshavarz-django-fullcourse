from django.urls import path
from .views import ArticleList, ArticleDetail, CategoryList, AuthorList

# --- prevent HardCode by app_name=""
app_name="blog"
urlpatterns = [
    # --- prevent HardCode by name=""
    path('', ArticleList.as_view(),name="home"),
    path('page/<int:page>', ArticleList.as_view(),name="home"),
    # path('', home,name="home"),
    # path('page/<int:page>', home,name="home"),
    path('article/<slug:slug>', ArticleDetail.as_view(),name="detail"),
    path('category/<slug:slug>', CategoryList.as_view(),name="category"),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(),name="category"),
    path('author/<slug:username>', AuthorList.as_view(),name="author"),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(),name="author"),
    # path('api', api,name="api"),

]
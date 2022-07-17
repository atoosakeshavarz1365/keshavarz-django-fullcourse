from django import template
from ..models import Category

register = template.Library()

#  --- this is simple tag
@register.simple_tag
def title():
    return "وبلاگ جنگویی"

# --- this is inclusion tag
@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return {
        "category":Category.objects.filter(status__in =[True])
    }

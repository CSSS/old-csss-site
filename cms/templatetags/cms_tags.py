from django import template

from cms.models import Category

register = template.Library()

@register.assignment_tag
def get_categories():
    return Category.objects.all()
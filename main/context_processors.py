from .models import Category, Setting
from django.template.loader import render_to_string


def load_categories(request):
    categories = Category.objects.filter(parent=None).all()
    children_query = Category.objects.filter(parent_id__in=[k.id for k in categories]).all()
    children = {}

    for child in children_query:
        if child.parent_id not in children:
            children[child.parent_id] = []

        children[child.parent_id].append(child)

    return {
        'categories': categories,
        'category_children': children
    }


def load_settings(request):
    return {
        'setting_{}'.format(item.key): item.value for item in Setting.objects.all()
    }

#
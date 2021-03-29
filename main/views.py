from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Setting


class MainIndex(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # ids = map(int, Setting.objects.get(key='main_side_categories').value.split(","))
        context['sidebar_menu'] = Category.objects.filter(on_sidebar=True)\
            .order_by('on_sidebar_order').all()

        return context


class MainCategory(TemplateView):
    template_name = 'main/category.html'

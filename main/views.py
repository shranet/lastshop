from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Category, Setting, Post


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


class MainPageRead(DetailView):
    post_id = None
    model = Post
    template_name = 'main/page.html'

    def get_object(self, queryset=None):
        if self.post_id is None:
            return super().get_object(queryset)

        return Post.objects.get(id=self.post_id)






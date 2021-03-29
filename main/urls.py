from django.urls import path
from django.views.generic import TemplateView
from .views import MainIndex, MainCategory


app_name = 'main'

urlpatterns = [
    path('', MainIndex.as_view(), name='index'),
    path('category/', MainCategory.as_view(), name='category')
]


from django.urls import path
from django.views.generic import TemplateView
from .views import MainIndex, MainCategory, MainPageRead


app_name = 'main'

urlpatterns = [
    path('', MainIndex.as_view(), name='index'),
    path('category/', MainCategory.as_view(), name='category'),
    path('about/', MainPageRead.as_view(post_id=1), name="about"),
    path('contact/', MainPageRead.as_view(post_id=2), name="contact"),
    path('page/<int:pk>/', MainPageRead.as_view(), name="read")
]



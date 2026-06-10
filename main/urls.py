from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.categories, name='categories'),
    path('category/<slug:category_slug>/', views.category_product_list, name='category_product_list'),
]
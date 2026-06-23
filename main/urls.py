from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.product_list, name='home'),
    path('category/<slug:category_slug>/', views.product_list, name='category_product_list'),
    path('<int:id>/<slug:product_slug>/', views.product_detail, name='product_detail')
]
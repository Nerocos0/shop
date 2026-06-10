from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Category, Product

def categories(request):
    categories = get_list_or_404(Category)
    return render(request, 'main/main_page.html', {'categories':categories})


def category_product_list(request, category_slug=None):
    products = Product.objects.filter(is_active = True)
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    return render(request, 'main/products/category_product_list.html', 
                  context={
                      'category':category,
                      'products':products
                  })
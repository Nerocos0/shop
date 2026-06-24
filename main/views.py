from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    products = Product.objects.filter(is_active = True)
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    else:
        products = products.order_by('-created_at')[:12]
    
    return render(request, 'main/product/product_list.html', 
                  context={
                      'category':category,
                      'products':products
                  })

def product_detail(request, id, product_slug):
    product = get_object_or_404(Product, id=id, slug=product_slug, is_active=True)
    return render(request, 'main/product/product_detail.html',
                  context={
                      'product':product,
                  })
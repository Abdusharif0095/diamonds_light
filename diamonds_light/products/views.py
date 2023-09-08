from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages
# from django.contrib.auth.forms import AuthenticationForm
from cart.forms import CartAddProductForm
from rest_framework.views import APIView
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product, Category
from slugify import slugify


class AddProduct(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('You are not authenticated to view this page!')

        context = {
            'product_form': ProductForm(),
        }

        return render(request=request, template_name='products/add_product.html', context=context)

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.slug = slugify(obj.name)
            obj.save()
            return redirect('home')
        else:
            context = {
                'product_form': form,
            }
            return render(request=request, template_name='products/add_product.html', context=context)


class GetCategory(APIView):
    def get(self, request, category_id, category_slug):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(is_active=True)
        if category_slug:
            category = get_object_or_404(Category, id=category_id, slug=category_slug)
            products = products.filter(category=category)

        context = {
            'products': products,
        }
        return render(request=request, template_name="products/category.html", context=context)


class GetProduct(APIView):
    def get(self, request, product_id, slug):
        product = get_object_or_404(Product, id=product_id,
                                    slug=slug, is_active=True)
        cart_product_form = CartAddProductForm()
        context = {
            'product': product,
            'cart_product_form': cart_product_form,
        }
        return render(request=request, template_name="products/product_detail.html", context=context)

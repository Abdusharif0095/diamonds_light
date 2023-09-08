from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from rest_framework.views import APIView


class CartAdd(APIView):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'],
                     )
            # print("is correct!")
            return redirect('cart:cart_detail')


class CartRemove(APIView):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')


class CartDetail(APIView):
    def get(self, request):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                initial={
                    'quantity': item['quantity'],
                    'update': True,
                }
            )

        return render(request, 'cart/detail.html', {'cart': cart})

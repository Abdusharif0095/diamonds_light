from django import template

from products.models import Category, Product

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.filter(is_active=True)


@register.simple_tag()
def get_products():
    return Product.objects.filter(is_active=True)


@register.filter(name='get_price')
def get_price(price, discount):
    if not discount:
        discount = 0
    return price - price * discount / 100

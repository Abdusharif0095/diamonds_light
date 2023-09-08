from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=forms.Textarea(attrs={'rows': 4, 'cols': 30}))

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category', 'stock', 'is_active', 'discount']
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'price': 'Цена',
            'image': 'Фото',
            'category': 'Категория',
            'stock': 'Количество',
            'is_active': 'В продаже',
            'discount': 'Скидка'
        }

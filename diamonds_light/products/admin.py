from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_show',
                    'is_active', 'created_at', 'updated_at']
    list_editable = ['is_active']
    prepopulated_fields = {'slug': ('name', )}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return None

    image_show.__name__ = "Картинка"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_show',
                    'abbreviated_description', 'price', 'category',
                    'stock', 'date_added', 'is_active', 'discount']
    list_filter = ['is_active', 'date_added']
    list_editable = ['price', 'stock', 'is_active']
    prepopulated_fields = {'slug': ('name',)}

    def abbreviated_description(self, obj):
        description = obj.description[:20]
        if len(obj.description) > 20:
            description += '...'

        return description

    abbreviated_description.__name__ = 'Описание'

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return None

    image_show.__name__ = "Картинка"


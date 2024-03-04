from django.contrib import admin

from products.models import (
    CategoryModel, BrandModel, SizeModel,
    ColorModel, TagModel, ProductModel, WishlistModel,
    ProductImage)

# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(BrandModel)
admin.site.register(SizeModel)
admin.site.register(ColorModel)
admin.site.register(TagModel)
admin.site.register(WishlistModel)
admin.site.register(ProductImage)

class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    inlines = [ProductImageInline]
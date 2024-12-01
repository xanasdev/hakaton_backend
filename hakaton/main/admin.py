from django.contrib import admin
from .models import *


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone_number')
    search_fields = ['name', 'surname', 'phone_number', 'description']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'supplier')
    search_fields = ['name', 'supplier']


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname','phone_number')
    search_fields = ('name', 'surname', 'phone_number')


admin.site.register(ProductPhotos)
admin.site.register(SupplierProfile, SupplierAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PurchasedProductsUsers)
admin.site.register(UserProfile, UserAdmin)
from django.contrib import admin
from network.models import Provider, Product, Branch

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'date_release']


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'country', 'town', 'street', 'house_number', 'register_form']
    list_filter = ['town']
    search_fields = ['name']


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'buyer', 'seller', 'products', 'debt', 'time']
    list_filter = ['name']
    search_fields = ['name']
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        """Функция для обнуления задолжности"""
        queryset.update(debt=0)
    clear_debt.description = "Очистить задолженность перед поставщиком"

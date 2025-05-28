from django.contrib import admin
from .models import Status, Type, Category, Subcategory, CashFlow


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_name',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'type')
    list_filter = ('type',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory_name', 'category')
    list_filter = ('category',)


@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'type', 'category', 'subcategory', 'amount')
    list_filter = ('status', 'type', 'category', 'subcategory')



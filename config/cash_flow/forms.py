from django import forms
from .models import Status, Type, Category, Subcategory, CashFlow
from django.core.exceptions import ValidationError


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = '__all__'


class CashFlowForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'description']

        def clean(self):
            cleaned_data = super().clean()
            type_obj = cleaned_data.get('type')
            category = cleaned_data.get('category')
            subcategory = cleaned_data.get('subcategory')

            if category and category.type != type_obj:
                raise ValidationError("Выбранная категория не относится к этому типу")

            if subcategory and subcategory.category != category:
                raise ValidationError("Выбранная подкатегория не относится к этой категории")

            return cleaned_data


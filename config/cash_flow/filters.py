import django_filters
from .models import CashFlow, Status, Type, Category, Subcategory
from django import forms


class CashFlowFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(
        field_name='date',
        label='Период',
        widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'class': 'form-control'},))

    class Meta:
        model = CashFlow
        fields = ['status', 'type', 'category', 'subcategory']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.filters['category'].extra.update({'queryset': Category.objects.none()})
        self.filters['subcategory'].extra.update({'queryset': Subcategory.objects.none()})
        if 'type' in self.data:
            try:
                self.filters['category'].extra['queryset'] = Category.objects.filter(type_id=int(self.data.get('type')))
            except (ValueError, KeyError):
                pass
        if 'category' in self.data:
            try:
                self.filters['subcategory'].extra['queryset'] = Subcategory.objects.filter(category_id=int(self.data.get('category')))
            except (ValueError, KeyError):
                pass

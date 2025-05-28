from django.urls import path
from .apps import CashFlowConfig
from .views import (CashFlowListView, CashFlowCreateView, CashFlowUpdateView, CashFlowDeleteView, DirectoriesListView,
                    StatusListView, StatusCreateView, StatusUpdateView, StatusDeleteView,
                    TypeListView, TypeCreateView, TypeUpdateView, TypeDeleteView,
                    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
                    SubcategoryListView, SubcategoryCreateView, SubcategoryUpdateView, SubcategoryDeleteView,
                    load_categories, load_subcategories)


app_name = CashFlowConfig.name


urlpatterns = [
    path('', CashFlowListView.as_view(), name='cashflow_list'),
    path('create/', CashFlowCreateView.as_view(), name='cashflow_create'),
    path('update/<int:pk>/', CashFlowUpdateView.as_view(), name='cashflow_update'),
    path('delete/<int:pk>/', CashFlowDeleteView.as_view(), name='cashflow_delete'),

    path('directories/', DirectoriesListView.as_view(), name='directories'),

    path('directories/status/', StatusListView.as_view(), name='status_list'),
    path('directories/status/create/', StatusCreateView.as_view(), name='status_create'),
    path('directories/status/update/<int:pk>/', StatusUpdateView.as_view(), name='status_update'),
    path('directories/status/delete/<int:pk>/', StatusDeleteView.as_view(), name='status_delete'),

    path('directories/type/', TypeListView.as_view(), name='type_list'),
    path('directories/type/create/', TypeCreateView.as_view(), name='type_create'),
    path('directories/type/update/<int:pk>/', TypeUpdateView.as_view(), name='type_update'),
    path('directories/type/delete/<int:pk>/', TypeDeleteView.as_view(), name='type_delete'),

    path('directories/category/', CategoryListView.as_view(), name='category_list'),
    path('directories/category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('directories/category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('directories/category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    path('directories/subcategory/', SubcategoryListView.as_view(), name='subcategory_list'),
    path('directories/subcategory/create/', SubcategoryCreateView.as_view(), name='subcategory_create'),
    path('directories/subcategory/update/<int:pk>/', SubcategoryUpdateView.as_view(), name='subcategory_update'),
    path('directories/subcategory/delete/<int:pk>/', SubcategoryDeleteView.as_view(), name='subcategory_delete'),

    path('ajax/load_categories/', load_categories, name='category_list'),
    path('ajax/load_subcategories/', load_subcategories, name='subcategory_list'),
]

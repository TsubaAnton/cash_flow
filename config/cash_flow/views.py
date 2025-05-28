from django.urls import reverse_lazy
from django_filters.views import FilterView
from .models import Status, Type, Category, Subcategory, CashFlow
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import CashFlowForm
from .filters import CashFlowFilter
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist


class CashFlowCreateView(CreateView):
    model = CashFlow
    form_class = CashFlowForm
    success_url = reverse_lazy('cash_flow:cashflow_list')


class CashFlowListView(FilterView, ListView):
    model = CashFlow
    filterset_class = CashFlowFilter
    template_name = 'cash_flow/cashflow_list.html'


class CashFlowUpdateView(UpdateView):
    model = CashFlow
    form_class = CashFlowForm
    success_url = reverse_lazy('cash_flow:cashflow_list')


class CashFlowDeleteView(DeleteView):
    model = CashFlow
    success_url = reverse_lazy('cash_flow:cashflow_list')


class DirectoryMixin(SuccessMessageMixin):
    template_name = 'cash_flow/directory_form.html'

    def get_tab_name(self):
        model_to_tab = {
            'status': 'status',
            'type': 'types',
            'category': 'categories',
            'subcategory': 'subcategories',
        }
        return model_to_tab.get(self.model.__name__.lower(), 'status')

    def get_success_url(self):
        tab = self.get_tab_name()
        return f"{reverse_lazy('cash_flow:directories')}?tab={tab}"


class BaseDeleteView(DeleteView):
    template_name = 'cash_flow/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success_url'] = self.get_success_url()
        return context


class StatusListView(ListView):
    model = Status
    template_name = 'cash_flow:directories.html'


class StatusCreateView(DirectoryMixin, CreateView):
    model = Status
    fields = ['status_name']


class StatusUpdateView(DirectoryMixin, UpdateView):
    model = Status
    fields = ['status_name']


class StatusDeleteView(BaseDeleteView):
    model = Status
    success_url = reverse_lazy('cash_flow:directories')


class TypeListView(ListView):
    model = Type
    template_name = 'cash_flow:directories.html'


class TypeCreateView(DirectoryMixin, CreateView):
    model = Type
    fields = ['type_name']


class TypeUpdateView(DirectoryMixin, UpdateView):
    model = Type
    fields = ['type_name']


class TypeDeleteView(BaseDeleteView):
    model = Type
    success_url = reverse_lazy('cash_flow:directories')


class CategoryListView(ListView):
    model = Category
    template_name = 'cash_flow:directories.html'


class CategoryCreateView(DirectoryMixin, CreateView):
    model = Category
    fields = ['type', 'category_name']


class CategoryUpdateView(DirectoryMixin, UpdateView):
    model = Category
    fields = ['type', 'category_name']


class CategoryDeleteView(BaseDeleteView):
    model = Category
    success_url = reverse_lazy('cash_flow:directories')


class SubcategoryListView(ListView):
    model = Subcategory
    template_name = 'cash_flow:directories.html'


class SubcategoryCreateView(DirectoryMixin, CreateView):
    model = Subcategory
    fields = ['category', 'subcategory_name']


class SubcategoryUpdateView(DirectoryMixin, UpdateView):
    model = Subcategory
    fields = ['subcategory', 'subcategory_name']


class SubcategoryDeleteView(BaseDeleteView):
    model = Subcategory
    success_url = reverse_lazy('cash_flow:directories')


class DirectoriesListView(TemplateView):
    template_name = 'cash_flow/directories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'status_list': Status.objects.all(),
            'type_list': Type.objects.all(),
            'category_list': Category.objects.all(),
            'subcategory_list': Subcategory.objects.all(),
        })
        return context


def load_categories(request):
    try:
        type_id = request.GET.get('type_id')
        if not type_id:
            return JsonResponse({'html': '<option value="">---------</option>'})

        categories = Category.objects.filter(type_id=int(type_id))
        context = {'categories': categories}
        html = render_to_string('cash_flow/includes/category_options.html', context)
        return JsonResponse({'html': html})

    except (ValueError, ObjectDoesNotExist):
        return JsonResponse({'html': '<option value="">---------</option>'})


def load_subcategories(request):
    try:
        category_id = request.GET.get('category_id')
        if not category_id:
            return JsonResponse({'html': '<option value="">---------</option>'})

        subcategories = Subcategory.objects.filter(category_id=int(category_id))
        context = {'subcategories': subcategories}
        html = render_to_string('cash_flow/includes/subcategory_options.html', context)
        return JsonResponse({'html': html})

    except (ValueError, ObjectDoesNotExist):
        return JsonResponse({'html': '<option value="">---------</option>'})
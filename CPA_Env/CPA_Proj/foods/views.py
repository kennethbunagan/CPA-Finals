from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Product, ProductDetails

class IndexView(generic.ListView):
    template_name = 'foods/index.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView):
    model = Product
    template_name = 'foods/detail.html'

class ProductCreate(CreateView):
    model = Product
    fields = ['productname']

class ProductUpdate(UpdateView):
    model = Product
    fields = ['productname']

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('foods:index')


class ProductDetailsCreate(CreateView):
    model = ProductDetails
    success_url = reverse_lazy('foods:index')
    fields = ['prod', 'price', 'weight']

class ProductDetailsUpdate(UpdateView):
    model = ProductDetails
    success_url = reverse_lazy('foods:index')
    fields = ['prod', 'price', 'weight']

class ProductDetailsDelete(DeleteView):
    model = ProductDetails
    success_url = reverse_lazy('foods:index')


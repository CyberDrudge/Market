from django.views.generic import ListView, DetailView
from .models import Products
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'products/list.html'

    def get_queryset(self):
        return Products.objects.all()


class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'products/detail.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Products, slug=slug)
        return instance

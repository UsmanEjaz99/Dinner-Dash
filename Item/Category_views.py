from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from Item.models import Category, Item
from django.views import View
from django.shortcuts import redirect, render
from .forms import CategoryForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class CategoryListView(ListView):
    model = Category
    template_name = 'Category_List.html'  # Template to display category list

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'Category_Form.html'  # Template for category creation

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'Category_Form.html'  # Template for category update
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')

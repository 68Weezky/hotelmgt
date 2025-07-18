from django.shortcuts import render
from .models import Category, MenuItem

def menu_index(request):
    categories = Category.objects.prefetch_related('items').all()
    return render(request, 'menu_index.html', {'categories': categories}) 
from django.shortcuts import render
from .models import BarMenuItem, BarGallery, BarCategory

# Create your views here.

def bar_index(request):
    categories = BarCategory.objects.prefetch_related('items').all()
    gallery = BarGallery.objects.all().order_by('-uploaded_at')
    return render(request, 'bar_index.html', {'categories': categories, 'gallery': gallery})

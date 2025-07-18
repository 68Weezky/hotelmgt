from django.shortcuts import render
from .models import StaffProfile

# Create your views here.

def staff_index(request):
    staff_profiles = StaffProfile.objects.all()
    return render(request, 'staff_index.html', {'staff_profiles': staff_profiles})

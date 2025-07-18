from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def contact_index(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Your message has been sent!')
        return redirect('contact_index')
    return render(request, 'contact_index.html', {'form': form})

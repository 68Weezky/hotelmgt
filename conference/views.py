from django.shortcuts import render, redirect
from .models import ConferenceRoom, ConferenceBooking
from .forms import ConferenceBookingForm
from django.contrib import messages

# Create your views here.

def conference_index(request):
    conference_room = ConferenceRoom.objects.first()
    form = ConferenceBookingForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Your conference room booking was successful!')
        return redirect('conference_index')
    return render(request, 'conference_index.html', {'conference_room': conference_room, 'form': form})

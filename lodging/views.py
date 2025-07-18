from django.shortcuts import render, redirect
from .models import RoomType, Room, Booking
from .forms import BookingForm
from django.contrib import messages

# Create your views here.

def lodging_index(request):
    room_types = RoomType.objects.prefetch_related('rooms').all()
    form = BookingForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        booking = form.save()
        # Mark the room as unavailable
        booking.room.is_available = False
        booking.room.save()
        messages.success(request, 'Your booking was successful!')
        return redirect('lodging_index')
    return render(request, 'lodging_index.html', {'room_types': room_types, 'form': form})

from django.db import models

# Create your models here.

class ConferenceRoom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    capacity = models.PositiveIntegerField()
    amenities = models.TextField(blank=True)
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='conference/', blank=True, null=True)

    def __str__(self):
        return self.name

class ConferenceBooking(models.Model):
    conference_room = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)
    booker_name = models.CharField(max_length=100)
    booker_email = models.EmailField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.booker_name} ({self.conference_room})"

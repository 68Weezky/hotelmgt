from django.db import models

# Create your models here.

class StaffProfile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='staff/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.role}"

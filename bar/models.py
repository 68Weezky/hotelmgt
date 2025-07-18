from django.db import models

# Create your models here.

class BarCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class BarMenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='bar/', blank=True, null=True)
    category = models.ForeignKey(BarCategory, on_delete=models.CASCADE, related_name='items', null=True, blank=True)

    def __str__(self):
        return self.name

class BarGallery(models.Model):
    image = models.ImageField(upload_to='bar/gallery/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption or f"Bar Image {self.id}"

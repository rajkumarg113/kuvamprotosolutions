from django.db import models

# Create your models here.
from django.db import models

class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100, blank=True)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    interest = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
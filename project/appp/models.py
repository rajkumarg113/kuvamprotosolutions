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




class Referral(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('qualified', 'Qualified (Tier 1)'),
        ('converted', 'Converted (Tier 2)'),
        ('paid', 'Paid'),
        ('rejected', 'Rejected'),
    ]

    # Referrer Details
    referrer_name = models.CharField(max_length=100)
    referrer_email = models.EmailField()
    referrer_phone = models.CharField(max_length=20)
    referrer_company = models.CharField(max_length=100, blank=True, null=True)

    # Referred Person/Company Details
    referred_name = models.CharField(max_length=100)
    referred_email = models.EmailField()
    referred_phone = models.CharField(max_length=20)
    referred_company = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Tracking
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referrer_name} referred {self.referred_name}"

class CareerApplication(models.Model):
   
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    experience = models.CharField(max_length=100)
    notice_period = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


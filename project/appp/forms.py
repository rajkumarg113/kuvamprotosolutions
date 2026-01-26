from django import forms
from .models import ContactRequest
from .models import Referral
from .models import CareerApplication

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'phone', 'company', 'preferred_date', 'preferred_time', 'interest']




class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = [
            'referrer_name', 'referrer_email', 'referrer_phone', 'referrer_company',
            'referred_name', 'referred_email', 'referred_phone', 'referred_company', 'notes'
        ]

class CareerApplicationForm(forms.ModelForm):
    class Meta:
        model = CareerApplication
        fields = [
            'name',
            'email',
            'phone',
            'location',
            'position',
            'experience',
            'notice_period',
            'message'
        ]
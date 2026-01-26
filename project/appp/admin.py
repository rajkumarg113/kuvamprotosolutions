from django.contrib import admin
from .models import CareerApplication, ContactRequest, Referral

# Register your models here.


# @admin.register(ContactRequest)
# class ContactRequestAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'interest', 'created_at')
#     list_filter = ('interest', 'created_at')
#     search_fields = ('name', 'email', 'phone')

admin.site.register(ContactRequest)
admin.site.register(Referral)
admin.site.register(CareerApplication)
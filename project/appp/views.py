from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, ReferralForm
import random
from django.http import JsonResponse, FileResponse
from django.core.mail import send_mail
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
import os

# Create your views here.
def home(request):
    return render(request,'appp/index.html')

def services(request):
    return render(request,'appp/services.html')

def products(request):
    return render(request,'appp/products.html')

def about(request):
    return render(request,'appp/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print("Form data:", request.POST)  # Debug print
        if form.is_valid():
            print("Form is valid")  # Debug print
            form.save()
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('contact')
        else:
            print("Form errors:", form.errors)  # Debug print
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'appp/contact.html', {'form': form})


def referral_view(request):
    if request.method == 'POST':
        form = ReferralForm(request.POST)
        print("Referral POST data:", request.POST)  # Debug print
        if form.is_valid():
            print("Referral Form is valid")  # Debug print
            form.save()
            messages.success(request, 'Referral submitted successfully! Thank you.')
            return redirect('referral') # Ensure 'referral' matches your urls.py name
        else:
            print("Referral Form errors:", form.errors)  # Debug print
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ReferralForm()
    
    return render(request, 'appp/referral.html', {'form': form})


def startup(request):
    return render(request, 'appp/startup.html')

def sme(request):
    return render(request, 'appp/sme.html')

def rnd(request):
    return render(request, 'appp/rnd.html')

def referral(request):
    return render(request, 'appp/referral.html')

def boxbuild (request):
    return render(request, 'appp/boxbuild.html')

def contractmanuf(request):
    return render(request, 'appp/contractmanuf.html')       

def injectionmould(request):
    return render(request, 'appp/injectionmould.html')        

def prototyping(request):
    return render(request, 'appp/prototyping.html')

def oem(request):
    return render(request, 'appp/oem.html')    

def diemould(request):
    return render(request, 'appp/diemould.html')   

# Products page




def refrigration_thermal(request):
    return render(request,'appp/refrigration_thermal.html')

def dc_compressor(request):
    return render(request,'appp/dc_compressor.html')
def industrial_cooling_distribution(request):
    return render(request,'appp/industrial_cooling_distribution.html')



def dustbin_prod(request):
    return render(request,'appp/dustbin_prod.html')
def dustbin1 (request):
    return render(request,'appp/dustbin1.html')
def dustbin2(request):
    return render(request,'appp/dustbin2.html')





def rugged_display(request):
    return render(request,'appp/rugged_display.html')

def inspection_duct_crawler(request):
    return render(request,'appp/inspection_duct_crawler.html')

def intrusion_alarm_system(request):
    return render(request,'appp/intrusion_alarm_system.html')

def fire_and_safety(request):
    return render(request,'appp/fire_and_safety.html')
def fire_safety1(request):
    return render(request, 'appp/fire_safety1.html')
def fire_safety2(request):
    return render(request, 'appp/fire_safety2.html')
def fire_safety3(request):
    return render(request, 'appp/fire_safety3.html')
@csrf_exempt
def send_otp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        name = data.get('name')
        
        # Generate OTP
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        
        # Store OTP in cache with 5 minutes expiration
        cache.set(f'otp_{email}', otp, 300)
        
        # Send email with OTP
        subject = 'Your Download OTP'
        message = f'Hello {name},\n\nYour OTP for downloading the product brochure is: {otp}\n\nThis OTP will expire in 5 minutes.'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@csrf_exempt
def verify_otp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        otp = data.get('otp')
        product_type = data.get('product_type')
        
        # Get stored OTP from cache
        stored_otp = cache.get(f'otp_{email}')
        
        if stored_otp and stored_otp == otp:
            cache.delete(f'otp_{email}')  # Delete used OTP
            return JsonResponse({'success': True, 'product_type': product_type})
            
        return JsonResponse({'success': False})
    return JsonResponse({'success': False})

def download_pdf(request):
    product_type = request.GET.get('type')
    
    # Define PDF paths for different products
    pdf_paths = {
        'dc_compressor': 'dc_compressor.pdf',
        'industrial_cooling_distribution':'industrial_cooling_distribution.pdf',
        'dustbin': 'dustbin.pdf',
        'inspection_duct_crawler': 'inspection_duct_crawler.pdf',
        'rugged_display': 'rugged_display.pdf',
        'intrusion_alarm_system': 'intrusion_alarm_system.pdf',
        'fire_and_safety': 'fire_and_safety.pdf'
    }
    
    # Get the correct PDF filename
    pdf_filename = pdf_paths.get(product_type)
    if not pdf_filename:
        return JsonResponse({'success': False, 'error': 'Invalid product type'})
    
    # Build the full file path
    file_path = os.path.join(settings.BASE_DIR, 'appp', 'static', 'appp', 'pdfs', pdf_filename)
    
    try:
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        return JsonResponse({'success': False, 'error': 'File not found'})

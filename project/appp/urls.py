from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('referral/', views.referral_view, name='referral'),
    path('startup/', views.startup, name='startup'),
    path('sme/', views.sme, name='sme'),
    path('rnd/', views.rnd, name='rnd'),
    path('careers/', views.careers_view, name='careers'),
    path('investor/', views.investor, name='investor'),
    path('investor/calculate/', views.calculate_investor, name='calculate_investor'),
    path('services/boxbuild/', views.boxbuild, name='boxbuild'),
    path('services/contractmanuf/', views.contractmanuf, name='contractmanuf'),
    path('services/injectionmould/', views.injectionmould, name='injectionmould'),
    path('services/prototyping/', views.prototyping, name='prototyping'),
    path('services/oem/', views.oem, name='oem'),
    path('services/diemould/', views.diemould, name='diemould'),


    path('products/refrigration_thermal',views.refrigration_thermal,name='refrigration_thermal'),
    path('products/refrigration_thermal/dc_compressor',views.dc_compressor,name="dc_compressor"),
    path('products/refrigration_thermal/industrial_cooling_distribution',views.industrial_cooling_distribution,name="industrial_cooling_distribution"),
    


    path('products/dustbin_prod',views.dustbin_prod,name='dustbin_prod'),
    path('products/dustbin_prod/dustbin1',views.dustbin1,name='dustbin1'),
    path('products/dustbin_prod/dustbin2',views.dustbin2,name='dustbin2'),
    
    path('products/inspectionduct_prod',views.inspectionduct_prod,name='inspectionduct_prod'),
    path('products/inspectionduct_prod/inspection_duct_crawler',views.inspection_duct_crawler,name='inspection_duct_crawler'),
    path('products/inspectionduct_prod/underwater_crawler',views.underwater_crawler,name='underwater_crawler'),
    
    path('products/intrusion_alarm_system',views.intrusion_alarm_system,name='intrusion_alarm_system'),
    
    path('products/fire_and_safety',views.fire_and_safety,name='fire_and_safety'),
    path('products/fire_and_safety/fire_safety1',views.fire_safety1,name='fire_safety1'),
    path('products/fire_and_safety/fire_safety2',views.fire_safety2,name='fire_safety2'),
    path('products/fire_and_safety/fire_safety3',views.fire_safety3,name='fire_safety3'),

    path('products/rugged_display',views.rugged_display,name='rugged_display'),

#
    path('send-otp/', views.send_otp, name='send_otp'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
]   

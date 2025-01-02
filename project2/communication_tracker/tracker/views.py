from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Company, CommunicationLog, CommunicationMethod
from datetime import date

def dashboard(request):
    companies = Company.objects.all()
    logs = CommunicationLog.objects.order_by('-date')[:5]
    return render(request, 'dashboard.html', {'companies': companies, 'logs': logs})

def calendar_page(request):
    logs = CommunicationLog.objects.all()
    return render(request, 'calendar.html', {'logs': logs})

def analytics_page(request):
    methods = CommunicationMethod.objects.all()
    return render(request, 'analytics.html', {'methods': methods})

def upload_page(request):
    if request.method == "POST":
        if 'company_submit' in request.POST:
            name = request.POST.get('company_name')
            location = request.POST.get('company_location')
            linkedin_profile = request.POST.get('company_linkedin')
            emails = request.POST.get('company_emails')
            phone_numbers = request.POST.get('company_phones')
            comments = request.POST.get('company_comments')
            communication_periodicity = request.POST.get('company_periodicity')
            Company.objects.create(
                name=name,
                location=location,
                linkedin_profile=linkedin_profile,
                emails=emails,
                phone_numbers=phone_numbers,
                comments=comments,
                communication_periodicity=communication_periodicity
            )
        elif 'method_submit' in request.POST:
            name = request.POST.get('method_name')
            description = request.POST.get('method_description')
            sequence = request.POST.get('method_sequence')
            mandatory = 'method_mandatory' in request.POST
            CommunicationMethod.objects.create(
                name=name,
                description=description,
                sequence=sequence,
                mandatory=mandatory
            )
        return redirect('upload_page')

    companies = Company.objects.all()
    methods = CommunicationMethod.objects.all()
    return render(request, 'upload_page.html', {'companies': companies, 'methods': methods})

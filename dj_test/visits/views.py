from random import randint
from django.shortcuts import render
from django.http import HttpResponse

from .models import Visitor, Visits

def get_client_ip(request):
    """Extract the client's IP address from the request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    visit = Visits.objects.first()
    visit.count += 1 if visit else 1
    visit.save()
    ip_address = get_client_ip(request)
    Visitor.objects.create(ip_address=ip_address)
    context = {
        "number_of_visits": visit.count if visit else 0,
        "ip_address": ip_address,
    }
    return render(request, 'index.html', context=context, status=200)
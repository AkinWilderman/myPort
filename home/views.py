from django.shortcuts import render
from .models import Home
from jobs.models import Job


def home(request):
    jobs = Job.objects.order_by('-date')
    homy = Home.objects
    return render(request, 'home/home.html', {'jobs': jobs, 'homy': homy})

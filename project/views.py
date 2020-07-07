from django.shortcuts import render
from .models import Project

# Create your views here.


def project(request):
    proj = Project.objects
    return render(request, 'project/project.html', {'proj': proj})

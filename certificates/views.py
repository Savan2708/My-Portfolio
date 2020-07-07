from django.shortcuts import render
from .models import Certificates


# Create your views here.


def certificates(request):
    certificates = Certificates.objects
    return render(request, 'certificates/certificates.html', {'certificates': certificates})

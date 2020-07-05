from django.shortcuts import render

# Create your views here.


def homepg(request):
    return render(request, 'home/homepg.html')

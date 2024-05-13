from django.shortcuts import render

# Create your views here.


def page_index(request):
    return render(request, "app_landing/about.html")


def page_beranda(request):
    return render(request, "app_dashboard/beranda.html")


def page_status(request):
    return render(request, "app_dashboard/status.html")

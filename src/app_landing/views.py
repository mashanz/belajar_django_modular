from django.shortcuts import render
from django.http import JsonResponse
from .form import UploadFileForm
import json


def agregasi(input):
    # business login
    result = input + 1
    return result


def page_landing(request):
    if request.method == "POST":
        print(request.POST)
        json_request = json.loads(request.body.decode("utf-8"))
        print(json_request)
        return JsonResponse({
            "message": "POST",
            "nama": json_request["nama"],
            "umut": json_request["umur"]
        })
    return render(request, "app_landing/index.html")

def page_semua(request):
    return render(request, "app_landing/semua.html")


def page_gambar(request):
    return render(request, "app_landing/gambar.html")

def page_video(request):
    return render(request, "app_landing/video.html")

def page_about(request, id: int = 0, year: int = 2024):
    name_param = ""
    if request.method == "POST":
        # print(request.POST.get("nama"))
        # print(request.FILES)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            nama = form.cleaned_data["nama"]
            file = form.cleaned_data["data_file"]
            print(f"nama -> {nama}")
            print(f"file -> {file}")
            return JsonResponse({
                "message": "POST",
                "nama": nama
            })
        else:
            return JsonResponse({
                "message": "POST",
                "error": form.errors
            })
    if request.method == "GET":
        id = request.GET.get("id_param", 0)
        name_param = request.GET.get("name_param", "Hans")
    context = {
        "NAMA": f"Hans {id} + {name_param}",
        "AGREGASI": agregasi(123),
        "YEAR": year,
    }
    
    return render(request, "app_landing/about.html", context)

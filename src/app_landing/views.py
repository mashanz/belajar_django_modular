from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def agregasi(input):
    # business login
    result = input + 1
    return result


def page_landing(request):
    # return render(request, "app_landing/index.html")
    return JsonResponse({"hello": "World", "data_dict": {"id": 1, "ar": [1, 2, 3, 4]}})


def page_about(request, id):
    if id:
        # ngapain gitu gitu
        pass
    context = {"NAMA": f"Hans {id}", "AGREGASI": agregasi(123)}
    return render(request, "app_landing/about.html", context)

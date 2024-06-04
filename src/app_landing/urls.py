from django.urls import path
from . import views

urlpatterns = [
    path("", views.page_landing),
    path("about", views.page_about),
    path("about/<int:id>", views.page_about),
    path("about/<int:id>/<int:year>", views.page_about),
    path("page_semua", views.page_semua),
    path("page_gambar", views.page_gambar),
    path("page_video", views.page_video)
]

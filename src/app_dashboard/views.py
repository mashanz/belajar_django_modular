from django.shortcuts import render

from .queries import book_create, book_read_all, book_read_one_by_id, book_update, book_delete


def page_index(request):
    # query = book_create("Hari Poter", "Je Ka Roling; DELETE FROM book;")
    # query = book_read_all(2)
    # query = book_read_one_by_id('1233e0e4-4cb7-430e-9f0c-7d7a0abc95a3')
    # query = book_update('1233e0e4-4cb7-430e-9f0c-7d7a0abc95a3', 'Hari muter muter', 'yaudahlah')
    # print(query.title, query.author)
    query = book_delete('1233e0e4-4cb7-430e-9f0c-7d7a0abc95a3')
    print(query)
    return render(request, "app_landing/about.html")


def page_beranda(request):
    return render(request, "app_dashboard/beranda.html")


def page_status(request):
    return render(request, "app_dashboard/status.html")

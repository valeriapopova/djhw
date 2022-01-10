from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def reader():
    csv_file = []
    with open('data-398-2018-08-30.csv') as file:
        reader_ = csv.reader(file)
        for r in reader_:
            if r[1] != 'Name' or r[4] != 'Street' or r[6] != 'District':
                csv_file.append({
                    'Name': r[1],
                    'Street': r[4],
                    'District': r[6]
                })
    return csv_file


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get("page", 1))
    content = reader()
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_number)
    context = {
         'bus_stations': page.object_list,
         'page': page,
    }
    return render(request, 'stations/index.html', context)

from multiprocessing import context
from django.shortcuts import render
from mywatchlist.models import Filmwatchlist
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_mywatchlist(request):
    data_barang_mywatchlist = Filmwatchlist.objects.all()
    context = {
        'list_barang': data_barang_mywatchlist,
        'nama': 'Muhammad Al Rivalda',
        'NPM' : '2106708961'
    }
    return render(request, "mywatchlist.html", context)



def show_xml(request):
    data = Filmwatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Filmwatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Filmwatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Filmwatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_html(request):
    data = Filmwatchlist.objects.all()
    total_film = 0
    for film in data:
        if film.watched:
            total_film +=1

    if total_film >= (len(data) - total_film):
        pesan = "Selamat, kamu sudah banyak menonton!"
    else :
        pesan = "Wah, kamu masih sedikit menonton!"
    
    context = {
        'list_barang': data,
        'nama': 'Muhammad Al Rivalda',
        'NPM' : '2106708961',
        'pesan' : pesan
    }
    
    return render(request,'mywatchlist.html', context);
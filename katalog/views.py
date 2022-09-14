from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog (request):
    return render(request,'katalog.html',context)


data_barang_katalog = CatalogItem.objects.all()
context = {
    'list_barang': data_barang_katalog,
    'nama': 'Muhammad Al Rivalda',
    'NPM' : '2106708961'
}
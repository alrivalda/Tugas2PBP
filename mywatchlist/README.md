

Link HTML :https://tugas2labpbpalrivalda.herokuapp.com/mywatchlist/html
Link XML : https://tugas2labpbpalrivalda.herokuapp.com/mywatchlist/xml
Link Json : https://tugas2labpbpalrivalda.herokuapp.com/mywatchlist/json

Jelaskan perbedaan antara JSON, XML, dan HTML!

Json - > Basisnya  notasi objek dalam javascripts, mudah dibaca, tidak pakai tag, karena mudah dibaca jadi kurang aman, hanya berisi data tanpa komen, sebagai transfer data
xml -> Baisnya markup languange(ML), susah dibaca,  memakai tag, lebih aman dipakai, bisa disii komen, digunakan sebagai transfer data
html ->basisnya markup languange (ML), isinya tag untuk menampilkan ke layar,bisa komen, digunakan untuk menampilkan layar

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
data itu bersifat dinamis sedangkan kebanyakan platform yang kita buat itu statis. Adanya delivery data memungkinkan untuk dilakukan perubahan data meski tampilan client tetap sama
hal ini akan membantu pengolahan data di backend sehingga penampilan data pada user bisa dinamis sesuai dengan pengolahan data yang kita lakukan di backend atau di server.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. pada django_procject.urls tambah path

 path('mywatchlist/', include('mywatchlist.urls'))
 
2. lalu bikin app baru dan menambahkan appnya ke installed apps pada django_projects.settings
3. bikin file urls.py pada direktori mywatchlist
    
    app_name ='watchlist'
urlpatterns = [
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_html, name='show_html'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),

]

4.  Pada views.py isi kode dengan kode dibawah ini

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
    
 5. pada models.py buat model data nya
    
    class Filmwatchlist(models.Model):
    watched = models.BooleanField()
    title =  models.CharField(max_length=255)
    rating =  models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    release_date = models.DateField()
    review = models.TextField()

   
6. bikin file html pada templates mywatchlist
7. bikin file berisi data yang akan ditampilkan dengan format json
8. edit file tests.py dan implementasikan testing
9. lakukan python manage.py makemigrations
10. python manage.py migrate
11. python manage.py loaddata (nama pada fixtures)
12. python manage.py runserver
13. push ke git


Screenshoot pada post man

![Screenshot (445)](https://user-images.githubusercontent.com/112602122/191657671-4c87cf8f-3e8f-4bad-9dc0-f89a315c5b88.png)![Screenshot (443)](https://user-images.githubusercontent.com/112602122/191657688-bdf38f06-7777-45bf-b963-9981e276a820.png)

![Screenshot (444)](https://user-images.githubusercontent.com/112602122/191657680-41843cef-f6c6-43b4-822b-181112cc5e70.png)


 

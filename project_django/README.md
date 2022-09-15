Nama  : Muhammad Al Rivalda

NPM   : 2106708961

Kelas : B


Link Heroku : (https://tugas2labpbpalrivalda.herokuapp.com/katalog/)

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

![x](https://user-images.githubusercontent.com/112602122/190295051-b1a3f1be-8bc9-4934-9ac8-0f6f70025c17.jpg)


Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environmet itu kita gunakan supaya beberapa library yang kita gunakan tidak bentrok dengan library yang sedang berjalan di global environment
sehingga pada app yang kita buat tidak bakal terjadi bug yang disebabkan oleh perbedaan versi django

Tetap bisa namun memiliki resiko bug yang sangat tinggi terutama ketika ada update versi dari library yang kita gunakan. Adanay virtual environment
membuat setiap proyek yang kita kerjakan memiliki modul mereka masing-masing sehingga tidak ada kemungkinann bentrok ketika kita gunakan


Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
1. Pertama , pada views  saya melakukan beberapa perubahan seperti melakukan import library
    
    
            from django.shortcuts import render
            from katalog.models import CatalogItem
    
    
  Lalu membuat fungsi untuk meminta request tampilan dimana saya membuat method yang mengakses models agar kita bisa mengakses materi
  
           def show_katalog(request):
           data_barang_katalog = CatalogItem.objects.all()
           context = {
              'list_barang': data_barang_katalog,
              'nama': 'Muhammad Al Rivalda',
              'npm' : '2106708961'
           }
           
   return render(request, "katalog.html", context)
 2. Pada katalog.html saya melakukan beberapa perubahan
    
    pertama saya menegdit bagian fill me dengan sebuah varibel
    
    
            <h5>Name: </h5>
            <p>Fill me!</p>

            <h5>Student ID: </h5>
            <p>Fill me!</p>
            
    
    menjadi
    
    
            <h5>Name: </h5>
            <p>{{nama}}</p>

            <h5>Student ID: </h5>
            <p>{{npm}}</p>
    
    
   Selain itu, saya juga mengedit isi tampilan tabel dengan menambah beberapa kategori serta melakukan penyesuaian nama variabel serta melakukan 
   iterasi pada data list_barang untuk menampilkan data pada tabel
   
           {% comment %} Add the data below this line {% endcomment %}
          {% for barang in list_barang %}
          <tr>
             <th>{{barang.item_name}}</th>
             <th>{{barang.item_price}}</th>
             <th>{{barang.item_stock}}</th>
             <th>{{barang.description}}</th>
             <th>{{barang.Rating}}</th>
             <th>{{barang.item_url}}</th>
          </tr>
          {% endfor %}
   
3. a. sebelum melakukan push atau run saya meunduh library env dengan

          python -m venv env

   b. lalu masuk ke folder env/Script dan melakukan perintah .\activate
   
   
   c. setelah itu saya melakukan downlod library yang ada pada requirements dengan cara
   
          pip install -r requirements.txt
   
   
   d. lalu saya melakukan run dengan cara
   
          python manage.py runserver
          
   e. lalu membuka website server lokal yang kita buat dengan menambah path /katalog dibelakangnya
   
          http://localhost:8000/katalog
          
 4. `a. Pada heroku saya buat app baru dengan nama tugas2pbpalrivalda
 
     b. lalu saya copy API keys di setting
     
     c. Lalu saya buka setting -> Secrets -> Action untuk menghubungkan github ke heroku
     
     d. Lalu saya menambah HEROKU_API_KEY dan HEROKU_APP_NAME beserta isinya
     
     e. Lalu saya kembali ke git dan cek action - workflows apakah berhasil atau tidak
     
     f. karena sudah berhasil saya coba openapp pada heroku dan ternyata hasilnya sudah berhasil
     
     
 

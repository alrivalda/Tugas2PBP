

apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
  Fungsinya sebagai autentifikasi. tag csrf token akan memuat token unik dimana digunakan untuk menghindari serangan dari luar terutama hacker. Token ini akan terus refresh setiap kita load atau melakukan request. Tanpa ada csrf maka tidak akan bisa ada eksekusi.
  misal kita ingin mengirim data atau POST maka tidak akan terkirim data tersebut
  
 Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
  bisa kok, adanya as table cuma lebih mengefisiensi kerja ditambah fungsi sebenarnya adalah merapikan table. Jadi, kalau mau manual bisa-bisa aja. 
  
 Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML. 
  Awalnya kita akan klik submit. Pada submit ini akan dicek apakah input yang kita masukkan valid sekaligus akan terjadi pengecekan csrf token. Jika benar maka akan lanjut ke view.py.
  Disini, akan terjadi proses seperti yang kita tulis seperti redirect ke halaman lain, atau akan memvalidasi user,dll. Nah, jika sudah benar maka data bisa disimpan pada database
  
  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
  
  1. Melakukan installasi apps todolist dan memasukanya ke apps setting.py
  2. Menambah path ke todolist pada urls.py di django_project
  3. Menambah semua path yang akan kita gunakan seperti pada soal yaitu utama, login, register, createtask, dan logout. Sebenarnya ada lagi yaitu untuk melakukan update dan delet task(soal bonus)
  4. Pada view kita lakukan pengolahan
   untuk login 
  
  def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('todolist:show_index')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
  
  untuk logout
  
  
def logout_user(request):
    logout(request)
    return redirect("todolist:login")
  
  untuk register
  
  def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)
  
 Untuk sementara sampi situ saja
4. Lanjut mengedit templates dimana kita akan membuat register.html, login.html
5. Mari buat fungsi untuk tampilan utama todolist
  
  @login_required(login_url="/todolist/login")
def show_index(request): 
    task = Task.objects.filter(user = request.user)
    context = {
        "list_task" : task,
    }
    return render (request,'todolist.html', context)

  butuh login untuk bisa masuk ke tampilan utama
  dan disini saya juga membuat tampilan todolist.html
  
  
  6. Pada models lakukan pengisian format data yaitu untuk user, waktu ,dekripsi, finish, judul
  7. Buat forms.py dan hubungkan dengan model
  8. Pada views buat method add task, deletetask, update task
  
  
@login_required(login_url="/todolist/login")
def create_task (request) :
    if request.method == "POST":
        task_form = create_Task(request.POST)
        if task_form.is_valid():
            createtask = task_form.save(commit=False)
            createtask.user = request.user
            messages.success(request, "Task succesfully created")
            createtask.save()
            return redirect("todolist:show_index")
    else:
        task_form = create_Task()
    context = {
        "task" : task_form
    }   
    return render(request,"createtask.html",context)

@login_required(login_url="/todolist/login")
def update_task(request ,pk):
    task = Task.objects.get(pk=pk)
    task.finished = not task.finished
    task.save()
    messages.success(request,"Succcesfully update")
    return redirect("todolist:show_index")

@login_required(login_url="/todolist/login")
def delete_task(request ,pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    messages.success(request,"Succcesfully delete")
    return redirect("todolist:show_index")

9. Buat cretetask.html
10. Pastikan tidak ada bug
 
  
  
  

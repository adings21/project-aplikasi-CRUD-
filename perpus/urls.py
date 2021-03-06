from unicodedata import name
from django.contrib import admin
from django.urls import path
from perpustakaan.models import *
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('buku/' , buku, name= 'buku'),
    path('tambah-buku/', tambah_buku, name= 'tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('kelompok/', kelompok, name= 'kelompok'),
    path('tambah-kelompok/', tambah_kelompok, name='tambah_kelompok'),
    path('kelompok/ubah/<int:id_kelompok>', ubah_kelompok, name='ubah_kelompok'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name= 'hapus_buku'),
    path('users/hapus/<int:id_user>', hapus_users, name= 'hapus_users'),
    path('kelompok/hapus/<int:id_kelompok>', hapus_kelompok, name= 'hapus_kelompok'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('signup/', signup, name='signup'),
    path('user/', users, name='users'),
    path('export/xls/',export_xls, name= 'export_xls'),
    path('export/xlsx/',export_xlsx, name= 'export_xlsx'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
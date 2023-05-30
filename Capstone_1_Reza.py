pasien = {
    'ID001' : {'Kode Pasien' : 'ID001',
           'Nama Pasien' : 'Joko',
           'Umur' : '38',
           'Diagnosa Penyakit' : 'Diare',
           'Nama Dokter' : 'Harry',
           'Tanggal Masuk' : '20230807'},
    'ID002' : {'Kode Pasien' : 'ID002',
           'Nama Pasien' : 'Arkan',
           'Umur' : '34',
           'Diagnosa Penyakit' : 'Diabetes',
           'Nama Dokter' : 'Syarif',
           'Tanggal Masuk' : '20230101'},
    'US003' : {'Kode Pasien' : 'US003',
           'Nama Pasien' : 'Missy',
           'Umur' : '29',
           'Diagnosa Penyakit' : 'Diabetes',
           'Nama Dokter' : 'Harry',
           'Tanggal Masuk' : '20220402'},
    'ID003' : {'Kode Pasien' : 'ID004',
           'Nama Pasien' : 'Kodir',
           'Umur' : '34',
           'Diagnosa Penyakit' : 'Hipertensi',
           'Nama Dokter' : 'Udin',
           'Tanggal Masuk' : '20220602'}
}

# Lain-Lain =================================================================================================
def kolom():
       print('_'*105)
       print(f'Kode Pasien\t|Nama Pasien \t|Umur\t\t|Diagnosa Penyakit\t|Nama Dokter \t|Tanggal Masuk\t|')
       print('_'*105)

def baris_data():
       for i in pasien:
              print(f'{pasien[i]["Kode Pasien"]}   \t|{pasien[i]["Nama Pasien"]}    \t|{pasien[i]["Umur"]}     \t|{pasien[i]["Diagnosa Penyakit"]}          \t|{pasien[i]["Nama Dokter"]}   \t|{pasien[i]["Tanggal Masuk"]}\t|')
       print('_'*105)


# MENU UTAMA ==================================================================================================
def menu():
       print()
       print('='*60)
       print('SELAMAT DATANG di DATA PASIEN RUMAH SAKIT A'.center(60,' '))
       print('='*60)
       print('Menu 1\t: Menampilkan Data Pasien Rumah Sakit A')
       print('Menu 2\t: Menambahkan Data Pasien Rumah Sakit A')
       print('Menu 3\t: Mengubah Data Pasien Rumah Sakit A')
       print('Menu 4\t: Menghapus Data Pasien Rumah Sakit A')
       print('Menu 5\t: Keluar')
       print('='*60)
       print()
       pilihan = input('Masukkan Angka Menu yang Ingin Dijalankan : ')
       if pilihan == '1':
              menu1()
       elif pilihan == '2':
              menu2()
       elif pilihan == '3':
              menu3()
       elif pilihan == '4':
              menu4()
       elif pilihan == '5':
              print()
              print('TERIMAKASIH TELAH MENGGUNAKAN PROGRAM DATA PASIEN RUMAH SAKIT A'.center(60,' '))
              print()
              exit()
       else :
              print()
              print('>< >< >< Masukkan Angka Sesuai Pada Pilihan Menu >< >< ><')
              print()
              menu()

# MENU 1 ====================================================================================================    
def menu1():
       if pasien == {}:
              print()
              print(' Tidak ada Data Pasien Rumah Sakit A, silahkan tambahkan data ')
              print()
              print(' Program secara otomatis ke menu 2 ')
              print()
              menu2()
       elif pasien != {}:
              print()
              print(' MENAMPILKAN DATA '.center(70,'='))
              print('1. Menampilkan seluruh data pasien Rumah Sakit A')
              print('2. Menampilkan data untuk kode pasien yang diinginkan pada Rumah Sakit A')
              print('3. Menampilkan suatu baris dengan memasukkan kata kunci pada data pasien Rumah Sakit A')
              print('4. Mengurutkan data berdasarkan Kode Pasien')
              print('5. Kembali ke Menu Utama')
              print('-'*70)
              pilihan = input('Masukkan angka pada opsi yang diinginkan : ')
              if pilihan == '1':
                     tampilkan_data()
              elif pilihan == '2':
                     sebagian_data()
              elif pilihan == '3':
                     nyari_data()
              elif pilihan == '4':
                     urut_kode()
              elif pilihan == '5':
                     menu()
              else :
                     print('>< >< >< Opsi yang anda inginkan tidak ada, mohon memilih opsi yang ada >< >< ><')
                     menu1()

# Menu 1 PILIHAN 1
def tampilkan_data():
       print()
       print('='*105)
       print(' DATA PASIEN RUMAH SAKIT A '.center(105,'-'))
       print('='*105)
       kolom()
       baris_data()
       menu1()

# Menu 1 PILIHAN 2
def sebagian_data():
       print()
       nomor = input('Masukkan Kode Pasien yang ingin ditampilkan : ').upper()
       print()
       if nomor in pasien :
              kolom()
              print(f'{pasien[nomor]["Kode Pasien"]}   \t|{pasien[nomor]["Nama Pasien"]}         \t|{pasien[nomor]["Umur"]}     \t|{pasien[nomor]["Diagnosa Penyakit"]}          \t|{pasien[nomor]["Nama Dokter"]}   \t|{pasien[nomor]["Tanggal Masuk"]}\t|')
              print()
              menu1()
       else :
              print()
              print('>< >< >< Kode Pasien yang anda input tidak terdaftar di Rumah Sakit A >< >< ><')
              print()
              sebagian_data()

# Menu 1 PILIHAN 3                 
def nyari_data():
       kolom()
       baris_data()
       print()
       b = input('Value yang ingin ditampilkan : ').title()
       for i in pasien:
              if b == pasien[i]['Kode Pasien']:
                     print(f'{pasien[i]["Kode Pasien"]}   \t|{pasien[i]["Nama Pasien"]}    \t|{pasien[i]["Umur"]}     \t|{pasien[i]["Diagnosa Penyakit"]}        \t|{pasien[i]["Nama Dokter"]}   \t|{pasien[i]["Tanggal Masuk"]}\t|')
              elif b == pasien[i]['Nama Pasien']:
                     print(f'{pasien[i]["Kode Pasien"]}   \t|{pasien[i]["Nama Pasien"]}    \t|{pasien[i]["Umur"]}     \t|{pasien[i]["Diagnosa Penyakit"]}        \t|{pasien[i]["Nama Dokter"]}   \t|{pasien[i]["Tanggal Masuk"]}\t|')
              elif b == pasien[i]['Umur']:
                     print(f'{pasien[i]["Kode Pasien"]}   \t|{pasien[i]["Nama Pasien"]}    \t|{pasien[i]["Umur"]}     \t|{pasien[i]["Diagnosa Penyakit"]}        \t|{pasien[i]["Nama Dokter"]}   \t|{pasien[i]["Tanggal Masuk"]}\t|')
              elif b == pasien[i]['Diagnosa Penyakit']:
                     print(f'{pasien[i]["Kode Pasien"]}   \t|{pasien[i]["Nama Pasien"]}    \t|{pasien[i]["Umur"]}     \t|{pasien[i]["Diagnosa Penyakit"]}        \t|{pasien[i]["Nama Dokter"]}   \t|{pasien[i]["Tanggal Masuk"]}\t|')
              elif b == pasien[i]['Nama Dokter']:
                     print(f'{pasien[i]["Kode Pasien"]}   \t|{pasien[i]["Nama Pasien"]}    \t|{pasien[i]["Umur"]}     \t|{pasien[i]["Diagnosa Penyakit"]}        \t|{pasien[i]["Nama Dokter"]}   \t|{pasien[i]["Tanggal Masuk"]}\t|')
              elif b == pasien[i]['Tanggal Masuk']:
                     print(f'{pasien[i]["Kode Pasien"]}   \t|{pasien[i]["Nama Pasien"]}    \t|{pasien[i]["Umur"]}     \t|{pasien[i]["Diagnosa Penyakit"]}        \t|{pasien[i]["Nama Dokter"]}   \t|{pasien[i]["Tanggal Masuk"]}\t|')
       print()
       nyari_lagi()


# Bagian dari function nyari_data
def nyari_lagi():
    print()
    lagi = input('Apakah anda ingin melakukan pencarian lagi? (YA/TIDAK) : ').upper()
    if lagi == 'YA':
       nyari_data()
    elif lagi == 'TIDAK':
       menu1()
    else:
       print()
       print('Mohon maaf inputan anda salah')
       print()
       nyari_lagi()


# Menu 1 PILIHAN 4
def urut_kode():
       kecil_besar = input('Apakah anda ingin mengurutkan secara ascending atau descending? (ASC/DESC) : ').upper()
       if kecil_besar == 'ASC':
              kolom()
              baris_data()
              print()
              print('Setelah data diurutkan berdasarkan Kode Pasien menjadi :')
              print()
              a = dict(sorted(pasien.items()))
              kolom()
              for i in a:
                     print(f'{a[i]["Kode Pasien"]}   \t|{a[i]["Nama Pasien"]}    \t|{a[i]["Umur"]}     \t|{a[i]["Diagnosa Penyakit"]}          \t|{a[i]["Nama Dokter"]}   \t|{a[i]["Tanggal Masuk"]}\t|')
              print()
              def yatidak():
                     ya_tidak = input('Apakah anda ingin menyimpan hasil tersebut? (YA/TIDAK) : ').upper()
                     if ya_tidak == 'YA':
                            global pasien
                            pasien = a
                            print('Tabel data berhasil diubah!!')
                            print()
                            menu1()
                     elif ya_tidak == 'TIDAK':
                            print()
                            print('Anda meninggalkan menu mengurutkan kode')
                            print()
                            menu1()
                     else:
                            print()
                            print('Maaf inputan anda salah')
                            yatidak()
              yatidak()
       elif kecil_besar == 'DESC':
              kolom()
              baris_data()
              print()
              print('Setelah data diurutkan berdasarkan Kode Pasien menjadi :')
              print()
              a = dict(sorted(pasien.items(), reverse=True))
              kolom()
              for i in a:
                     print(f'{a[i]["Kode Pasien"]}   \t|{a[i]["Nama Pasien"]}    \t|{a[i]["Umur"]}     \t|{a[i]["Diagnosa Penyakit"]}          \t|{a[i]["Nama Dokter"]}   \t|{a[i]["Tanggal Masuk"]}\t|')
              print()
              def yatidak():
                     ya_tidak = input('Apakah anda ingin menyimpan hasil tersebut? (YA/TIDAK) : ').upper()
                     if ya_tidak == 'YA':
                            global pasien
                            pasien = a
                            print('Tabel data berhasil diubah!!')
                            print()
                            menu1()
                     elif ya_tidak == 'TIDAK':
                            print()
                            print('Anda meninggalkan menu mengurutkan kode')
                            print()
                            menu1()
                     else:
                            print()
                            print('Maaf inputan anda salah')
                            yatidak()
              yatidak()
       else:
              print()
              print('Maaf, inputan anda salah')
              urut_kode()



# MENU 2 =====================================================================================================================================
def menu2():
       print()
       print(' MENAMBAH DATA PADA RUMAH SAKIT A '.center(70,'='))
       print('1. Menambah data pasien Rumah Sakit A')
       print('2. Kembali ke Menu Utama')
       print('-'*70)
       pilihan = input('Masukkan angka pada opsi yang diinginkan : ')
       if pilihan == '1':
              menambah_data()
       elif pilihan == '2':
              menu()
       else :
              print()
              print('>< >< >< Opsi yang anda inginkan tidak ada, mohon memilih opsi yang ada >< >< ><')
              print()
              menu2()

# Menu 2 PILIHAN 1
def menambah_data():
       print()
       nopasien = input('Masukkan Kode Pasien baru yang ingin ditambahkan : ').upper()
       print()
       if len(nopasien) == 5 :
              if nopasien.isalpha() == True:
                     print()
                     print('Kode Pasien terdiri dari kombinasi huruf dan angka!! ')
                     print()
                     menambah_data()
              elif nopasien.isdigit() == True:
                     print()
                     print('Kode Pasien terdiri dari kombinasi huruf dan angka!! ')
                     print()
                     menambah_data()
              elif nopasien.isalnum() == True:
                     if nopasien in pasien:
                            print()
                            print(' Maaf Kode Pasien yang anda masukkan sudah terdaftar ')
                            print()
                            menambah_data()
                     elif nopasien not in pasien:
                            print()
                            nama = input('Masukkan Nama Pasien: ').title()
                            umur = input('Masukkan Umur: ')
                            penyakit = input('Masukkan Diagnosa Penyakit Pasien: ').title()
                            dokter = input('Masukkan Nama Dokter: ').title()
                            masuk = input('Masukkan tanggal masuk pasien (YYYYMMDD) : ')
                            pasien2 = {
                                   nopasien : {'Kode Pasien' : nopasien,
                                   'Nama Pasien' : nama,
                                   'Umur' : umur,
                                   'Diagnosa Penyakit' : penyakit,
                                   'Nama Dokter' : dokter,
                                   'Tanggal Masuk' : masuk}
                            }
                            kolom()
                            for i in pasien2:
                                   print(f'{pasien2[i]["Kode Pasien"]}   \t|{pasien2[i]["Nama Pasien"]}    \t|{pasien2[i]["Umur"]}     \t|{pasien2[i]["Diagnosa Penyakit"]}            \t|{pasien2[i]["Nama Dokter"]}   \t|{pasien2[i]["Tanggal Masuk"]}\t|')
                            print()
                            def ya_tidak():
                                   pilihan = input('Apakah anda ingin menambahkan data tersebut? (YA/TIDAK) : ').upper()
                                   if pilihan == 'YA':
                                          pasien.update(pasien2)
                                          print()
                                          print(f'Data Pasien {nopasien} berhasil ditambahkan ')
                                          print()
                                          menu2()
                                   elif pilihan == 'TIDAK':
                                          print()
                                          print(f'Data Pasien {nopasien} batal ditambahkan')
                                          print()
                                          menu2()
                                   else :
                                          print()
                                          print('Inputan anda salah, silahkan masukkan inputan yang benar')
                                          print()
                                          ya_tidak()
                            ya_tidak()
       else:
              print()
              print(' Masukkan 5 karakter untuk mengisi Kode Pasien ')
              print()
              menambah_data()

# MENU 3 ==========================================================================================================================
def menu3():
       if pasien == {}:
              print()
              print(' Tidak ada Data Pasien Rumah Sakit A, silahkan tambahkan data ')
              print()
              print(' Program secara otomatis ke menu 2 ')
              print()
              menu2()
       elif pasien != {}:
              print()
              print(' MENGUBAH DATA PADA RUMAH SAKIT A '.center(70,'='))
              print('1. Mengubah data pasien Rumah Sakit A')
              print('2. Kembali ke Menu Utama')
              print('-'*70)
              pilihan = input('Masukkan angka pada opsi yang diinginkan : ')
              if pilihan == '1':
                     mengubah_data()
              elif pilihan == '2':
                     menu()
              else :
                     print()
                     print('>< >< >< Opsi yang anda inginkan tidak ada, mohon memilih opsi yang ada >< >< ><')
                     print()
                     menu3()

# Menu 3 PILIHAN 1
def mengubah_data():
       print()
       print('='*105)
       print(' DATA PASIEN RUMAH SAKIT A '.center(105,'-'))
       print('='*105)
       kolom()
       baris_data()
       print()
       nopasien = input('Masukkan Kode Pasien yang ingin diubah : ').upper()
       print()
       if nopasien not in pasien:
              print()
              print(f'Kode Pasien {nopasien} tidak terdaftar ')
              print()
              mengubah_data()
       elif nopasien in pasien:
              kolom()
              print(f'{pasien[nopasien]["Kode Pasien"]}   \t|{pasien[nopasien]["Nama Pasien"]}       \t|{pasien[nopasien]["Umur"]}     \t|{pasien[nopasien]["Diagnosa Penyakit"]}          \t|{pasien[nopasien]["Nama Dokter"]}   \t|{pasien[nopasien]["Tanggal Masuk"]}\t|')
              print()
              def ubah_isi():
                     kode = input('Masukkan Nama kolom yang ingin diubah : ').title()
                     if kode not in pasien[nopasien]:
                            print()
                            print('Nama kolom yang anda masukkan salah ')
                            print()
                            ubah_isi()
                     elif kode == 'Kode Pasien':
                            print('Maaf anda tidak bisa merubah data Kode Pasien ')
                            print()
                            ubah_isi()
                     elif kode == 'Tanggal Masuk':
                            print('Maaf anda tidak bisa merubah tanggal masuk pasien ')
                            print()
                            ubah_isi()
                     else:
                            print()
                            baru = input(' Masukkan isian baru : ').title()
                            def ya_tidak():
                                   yakin = input(' Apakah anda yakin? (YA/TIDAK) : ').upper()
                                   if yakin == 'YA':
                                          pasien[nopasien][kode] = baru
                                          menu3()
                                   elif yakin == 'TIDAK':
                                          print()
                                          print(f'Inputan Kode Pasien anda : {nopasien}, Nama Kolom : {kode} dan Isi : {baru} telah dibatalkan untuk mengubah data ')
                                          print()
                                          menu3()
                                   else :
                                          print()
                                          print('Inputan yang anda masukkan salah ')
                                          print()
                                          ya_tidak()
                            ya_tidak()
              ubah_isi()

# MENU 4 =========================================================================================================================
def menu4():
       if pasien == {}:
              print()
              print(' Tidak ada Data Pasien Rumah Sakit A, silahkan tambahkan data ')
              print()
              print(' Program secara otomatis ke menu 2 ')
              print()
              menu2()
       elif pasien != {}:
              print()
              print(' MENGHAPUS DATA PADA RUMAH SAKIT A '.center(70,'='))
              print('1. Menghapus data pasien Rumah Sakit A')
              print('2. Menghapus seluruh data pasien Rumah Sakit A')
              print('3. Kembali ke Menu Utama')
              print('-'*70)
              pilihan = input('Masukkan angka pada opsi yang diinginkan : ')
              if pilihan == '1':
                     menghapus_data()
              elif pilihan == '2':
                     hapus_semua()
              elif pilihan == '3':
                     menu()
              else :
                     print()
                     print('>< >< >< Opsi yang anda inginkan tidak ada, mohon memilih opsi yang ada >< >< ><')
                     print()
                     menu4()

# Menu 4 PILIHAN 1
def menghapus_data():
       if pasien == {}:
              print()
              print(' Tidak ada Data Pasien Rumah Sakit A, silahkan tambahkan data ')
              print()
              print(' Program secara otomatis ke menu 2 ')
              print()
              menu2()
       elif pasien != {}:
              print()
              print('='*105)
              print(' DATA PASIEN RUMAH SAKIT A '.center(105,'-'))
              print('='*105)
              kolom()
              baris_data()
              nopasien = input(' Masukkan Kode Pasien untuk menghapus data Kode Pasien tersebut : ').upper()
              if nopasien in pasien:
                     kolom()
                     print(f'{pasien[nopasien]["Kode Pasien"]}   \t|{pasien[nopasien]["Nama Pasien"]}       \t|{pasien[nopasien]["Umur"]}     \t|{pasien[nopasien]["Diagnosa Penyakit"]}          \t|{pasien[nopasien]["Nama Dokter"]}\t|{pasien[nopasien]["Tanggal Masuk"]}\t|')
                     print()
                     def ya_tidak():
                            yakin = input(' Apakah anda yakin ingin menghapus data pasien tersebut? (YA/TIDAK) : ').upper()
                            if yakin == 'YA':
                                   del pasien[nopasien]
                                   print()
                                   print(f' Data Kode Pasien : {nopasien}, telah berhasil dihapus ')
                                   print()
                                   menu4()
                            elif yakin == 'TIDAK':
                                   print()
                                   print(f' Data Kode Pasien : {nopasien}, tidak dihapus ')
                                   print()
                                   menu4()
                            else :
                                   print()
                                   print(' Inputan yang anda masukkan salah ')
                                   print()
                                   ya_tidak()
                     ya_tidak()
              elif nopasien not in pasien:
                     print()
                     print(' Kode Pasien yang anda masukkan tidak terdaftar ')
                     print()
                     menghapus_data()

# Menu 4 PILIHAN 2
def hapus_semua():
       if pasien == {}:
              print()
              print(' Tidak ada Data Pasien Rumah Sakit A, silahkan tambahkan data ')
              print()
              print(' Program secara otomatis ke menu 2 ')
              print()
              menu2()
       elif pasien != {}:
              print()
              print('='*105)
              print(' DATA PASIEN RUMAH SAKIT A '.center(105,'-'))
              print('='*105)
              kolom()
              baris_data()
              def ya_tidak():
                     yakin = input(' Apakah anda yakin ingin menghapus data pasien tersebut? (YA/TIDAK) : ').upper()
                     if yakin == 'YA':
                            pasien.clear()
                            print()
                            print(f' Data Pasien Rumah Sakit A telah berhasil dihapus ')
                            print()
                            print(' Program Kembali Ke Menu ')
                            print()
                            menu()
                     elif yakin == 'TIDAK':
                            print()
                            print(f' Data Pasien Rumah Sakit A tidak dihapus ')
                            print()
                            menu4()
                     else :
                            print()
                            print(' Inputan yang anda masukkan salah ')
                            print()
                            ya_tidak()
              ya_tidak()


menu()

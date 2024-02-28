# 1. Presentasi 25
# 2. Fitur Create 15
# 3. Fitur Read 15
# 4. Fitur Update 20
# 5. Fitur Delete 15
# melakukan dokumentasi

# Case Study
# Data nilai siswa
# format.py
# upload ke GitHub
#
from tabulate import tabulate
import os

# membuat database dengan variabel data_siswa menggunakan collection data type nested dictionary
# dengan begitu data dapat dipanggil menggunakan NIS sebagai Primary Key, dan juga memiliki beberapa key lainnya yang bisa dipanggil
# setelah melakukan looping
data_siswa = {
    14100: {'Nama': 'Banu Baskara', 'Kelas': '12A', 'Gender': 'L', 'Nilai MTK': 90, 'Nilai Fisika': 66, 'Nilai Biologi': 85},
    14101: {'Nama': 'Jay', 'Kelas': '12B', 'Gender': 'L', 'Nilai MTK': 73, 'Nilai Fisika': 85, 'Nilai Biologi': 72},
    13982: {'Nama': 'Rey Bones', 'Kelas': '12E', 'Gender': 'L', 'Nilai MTK': 77, 'Nilai Fisika': 95, 'Nilai Biologi': 66},
    13761: {'Nama': 'Naufal G B', 'Kelas': '12F', 'Gender': 'L', 'Nilai MTK': 60, 'Nilai Fisika': 74, 'Nilai Biologi': 92},
    14023: {'Nama': 'Salma Nisrina', 'Kelas': '12A', 'Gender': 'P', 'Nilai MTK': 86, 'Nilai Fisika': 73, 'Nilai Biologi': 85},
    13205: {'Nama': 'Sasi', 'Kelas': '12C', 'Gender': 'P', 'Nilai MTK': 74, 'Nilai Fisika': 90, 'Nilai Biologi': 75}
}

data_remed = dict()

# membuat dict kosong untuk menampung data backup
backup_data = dict()

def data_recovery(backup_data):
    global data_siswa # dengan global variabel membuat data_siswa akan terubah dengan value dari backup_data.copy()
    data_siswa = backup_data
    return data_siswa


# Menyimpan backup data saat program dimulai
backup_data = data_siswa.copy()

# membuat list agar dapat dilakukan visualisasi data secara tabular menggunakan library tabulate
def listing():
    list_siswa = [[nis, siswa['Nama'], siswa['Kelas'], siswa['Gender'], siswa['Nilai MTK'], siswa['Nilai Fisika'], siswa['Nilai Biologi']] for nis, siswa in data_siswa.items()]
    return list_siswa

def listing_mtk_sorted():
    list_siswa = [[nis, siswa['Nama'], siswa['Kelas'], siswa['Gender'], siswa['Nilai MTK']] for nis, siswa in sorted_data.items()]
    return list_siswa

def listing_mtk():
    list_siswa = [[nis, siswa['Nama'], siswa['Kelas'], siswa['Gender'], siswa['Nilai MTK']] for nis, siswa in data_remed.items()]
    return list_siswa

def listing_fisika():
    list_siswa = [[nis, siswa['Nama'], siswa['Kelas'], siswa['Gender'], siswa['Nilai Fisika']] for nis, siswa in data_remed.items()]
    return list_siswa

def listing_biologi():
    list_siswa = [[nis, siswa['Nama'], siswa['Kelas'], siswa['Gender'], siswa['Nilai Biologi']] for nis, siswa in data_remed.items()]
    return list_siswa

# membuat fungsi untuk memberikan output ketika input tidak valid
def inputan_tidak_valid():
    os.system('cls')
    print('Inputan Tidak Valid, Silahkan Pilih Kembali !')

# fungsi untuk melakukan viewing data dan setelahnya akan ada pilihan untuk kembali ke sub mmnu
def sub_sorting():
    mtk_sorting_back = input('\n\nKembali Ke Menu Sorting ? [Masukan Apa Saja]\n').upper()
    if mtk_sorting_back == 'Y':
        os.system('cls')
        print('Kembali Pada Sub Menu Sorting')
    else:
        os.system('cls')
        print('Kembali Pada Sub Menu Sorting')

# fungsi untuk kembali ke menu sorting
def sorting_back():
    os.system('cls')
    print('Kembali Ke Menu Sorting')

# fungsi ini untuk memfilter 'Nilai MTK' yang kurang dari 75
def filter_nilai_mtk(data_siswa):
    filtered_data = {nomor: siswa for nomor, siswa in data_siswa.items() if siswa['Nilai MTK'] < 75}
    return filtered_data

# fungsi ini untuk memfilter 'Nilai Fisika' yang kurang dari 75
def filter_nilai_fisika(data_siswa):
    filtered_data = {nomor: siswa for nomor, siswa in data_siswa.items() if siswa['Nilai Fisika'] < 75}
    return filtered_data

# fungsi ini untuk memfilter 'Nilai Biologi' yang kurang dari 75
def filter_nilai_biologi(data_siswa):
    filtered_data = {nomor: siswa for nomor, siswa in data_siswa.items() if siswa['Nilai Biologi'] < 75}
    return filtered_data

# menggunakan while True sehingga program akan terus berjalan sampai kondisi salah atau break (bisa digunakan berkali-kali)
while True:
    print('='*60)
    print(f'{"Rekap Nilai Siswa Kelas 12 SMAN 800 Bandung":^60}')
    print('='*60)
    # MENU UTAMA
    print(f'\n1. Report Nilai Siswa\n2. Menambah Data Siswa\n3. Mengubah Data Siswa\n4. Menghapus Data Siswa\n5. Data Rollback\n\n0. Keluar Dari Program')
    menu_input = input('\n\nSilahkan Pilih Menu: ')
    os.system('cls') # digunakan untuk clear pada terminal, sehingga secara tampilan tidak berantakan
    if menu_input == '1': # memasuki menu read
        os.system('cls')
        # READ
        while True: # diberikan  loop yang bertindak sebagai  filter/cari data 
            print('='*40)
            print(f'{"REPORT NILAI SISWA":^40}')       
            print('='*40)
            # menu read
            print(f'\n1. Nilai Seluruh Siswa\n2. Siswa Tertentu\n3. Sorting\n4. Filtering\n5. Kembali Ke Menu Utama\n\n0. Keluar Dari Program')
            menu_read = input('\n\nSilahkan Pilih Menu: ')
            os.system('cls')
            if menu_read == '1':
                os.system('cls')
                print(f'\n{"Berikut Nilai Seluruh Siswa Kelas 12":^90}')
                # menggunakan tabulate untuk membuat data secara tabular yang baik
                # dikarenakan tabulate perlu menggunakan tipe data list, maka data diubah menjadi list dengan fungsi lsting
                # sehinga
                print(tabulate(listing(), headers=["NIS", "Nama", "Kelas", "Gender", "Nilai MTK", "Nilai Fisika", "Nilai Biologi"], tablefmt='fancy_grid'))
                menu_read_back = input('\n1. Kembali Ke Menu Report Nilai Siswa\n2. Kembali Ke Menu Utama\n\n0. Keluar Dari Program\n\nSilahkan Pilih Nomor: ')
                if menu_read_back == '1':
                    os.system('cls')
                    continue
                elif menu_read_back == '2':
                    os.system('cls')
                    break
                elif menu_read_back == '0':
                    exit()
                else:
                    inputan_tidak_valid()
            elif menu_read == '2':
                nis_input = input('Masukkan NIS: ')
                if not nis_input.isnumeric(): # membuat kondisi ketika salah akan mengulangi loop, sehingga ketika benar program flow teterus berjalan
                    os.system('cls')
                    print('NIS Harus Berupa Angka')
                    continue
                nis_output = int(nis_input) # setelah kondisi salah terlewati baru saya casting, sehingga tidak ada eror
                siswa_terpilih = data_siswa.get(nis_output) # jika NIS tidak ada, maka outputnya adalah none, maka akan masuk ke kondisi else
                if siswa_terpilih:
                    print(tabulate([[nis_output, siswa_terpilih['Nama'], siswa_terpilih['Kelas'], siswa_terpilih['Gender'], siswa_terpilih['Nilai MTK']]], headers=["NIS", "Nama", "Kelas", "Gender", "Nilai"], tablefmt='fancy_grid'))
                    sub_sorting()
                else:
                    os.system('cls')
                    print(f"Tidak Ada Data Siswa Dengan NIS {nis_output}")
                    continue
            elif menu_read == '3':
                while True:
                    print('='*40)
                    print(f'{"SORTING":^40}')       
                    print('='*40)
                    sorting_input = input('\n1. Urutkan Berdasarkan Nilai MTK\n2. Urutkan Berdasarkan Nilai Fisika\n3. Urutkan Berdasarkan Nilai Biologi\n4. Kembali Ke Menu Report Nilai Siswa\n\nPilihan Nomor: ')
                    os.system('cls')
                    if sorting_input == '1':
                        while True:
                            print('='*40)
                            print(f'{"SORTING BERDASARKAN NILAI MTK":^40}')       
                            print('='*40)
                            mtk_urut = input('\n1. Diurutkan Berdasarkan Nilai Terbesar\n2. Diurutkan Berdasrkan Nilai Terkecil\n3. Kembali Ke Menu Sorting\n\nPilihan Nomor: ')
                            if mtk_urut == '1':
                                os.system('cls')
                                sorted_data = dict(sorted(data_siswa.items(), key=lambda x: x[1]['Nilai MTK'], reverse=True))
                                list_siswa = [[nis, siswa['Nama'], siswa['Kelas'], siswa['Gender'], siswa['Nilai MTK']] for nis, siswa in sorted_data.items()]
                                print('Berikut Data Siswa Dengan Nilai MTK Terbesar Hingga Terkecil\n')
                                print(tabulate(list_siswa, headers=["NIS", "Nama", "Kelas", "Gender", "Nilai MTK"], tablefmt='fancy_grid'))
                                sub_sorting()
                            elif mtk_urut == '2':
                                os.system('cls')
                                sorted_data = dict(sorted(data_siswa.items(), key=lambda x: x[1]['Nilai MTK']))
                                list_siswa = [[nis, siswa['Nama'], siswa['Kelas'], siswa['Gender'], siswa['Nilai MTK']] for nis, siswa in sorted_data.items()]
                                print('Berikut Data Siswa Dengan Nilai MTK Terkecil Hingga Terbesar\n')
                                print(tabulate(list_siswa, headers=["NIS", "Nama", "Kelas", "Gender", "Nilai MTK"], tablefmt='fancy_grid'))
                                sub_sorting()
                            elif mtk_urut == '3':
                                sorting_back()
                                break
                            else:
                                inputan_tidak_valid()
                                continue
                    elif sorting_input == '2':
                        while True:
                            print('='*40)
                            print(f'{"SORTING BERDASARKAN NILAI FISIKA":^40}')       
                            print('='*40)
                            fisika_urut = input('\n1. Diurutkan Berdasarkan Nilai Terbesar\n2. Diurutkan Berdasrkan Nilai Terkecil\n3. Kembali Ke Menu Sorting\n\nPilihan Nomor: ')
                            os.system('cls')
                            if fisika_urut == '1':
                                sorted_data = dict(sorted(data_siswa.items(), key=lambda x: x[1]['Nilai Fisika'], reverse=True))
                                # melakukan sorting menggunakan lambda dengan mengambil Values dari Nilai Fisika, sehingga data
                                # diurutkan dari yang paling besar ke terkecil, karena reverse = True
                                list_siswa = [[nis, siswa['Nama'], siswa['Kelas'], siswa['Gender'], siswa['Nilai Fisika']] for nis, siswa in sorted_data.items()]
                                print('Berikut Data Siswa Dengan Nilai Fisika Terbesar Hingga Terkecil\n')
                                print(tabulate(list_siswa, headers=["NIS", "Nama", "Kelas", "Gender", "Nilai Fisika"], tablefmt='fancy_grid'))
                                sub_sorting()
                            elif fisika_urut == '2':
                                sorted_data = dict(sorted(data_siswa.items(), key=lambda x: x[1]['Nilai Fisika']))
                                # melakukan sorting menggunakan lambda dengan mengambil Values dari Nilai Fisika, sehingga data
                                # diurutkan dari yang paling terkecil ke terbesar, karena reverse = False
                                list_siswa = [[nis, siswa['Nama'], siswa['Kelas'], siswa['Gender'], siswa['Nilai Fisika']] for nis, siswa in sorted_data.items()]
                                print('Berikut Data Siswa Dengan Nilai Fisika Terkecil Hingga Terbesar\n')
                                print(tabulate(list_siswa, headers=["NIS", "Nama", "Kelas", "Gender", "Nilai Fisika"], tablefmt='fancy_grid'))
                                sub_sorting()
                            elif fisika_urut == '3':
                                sorting_back()
                                break
                            else:
                                inputan_tidak_valid()
                                continue
                    elif sorting_input == '3':
                        while True:
                            biologi_urut = input('\n1. Diurutkan Berdasarkan Nilai Terbesar\n2. Diurutkan Berdasrkan Nilai Terkecil\n3. Kembali Ke Menu Sorting\n\nPilihan Nomor: ')
                            os.system('cls')
                            if biologi_urut == '1':
                                sorted_data = dict(sorted(data_siswa.items(), key=lambda x: x[1]['Nilai Biologi'], reverse=True))
                                list_siswa = [[nis, siswa['Nama'], siswa['Kelas'], siswa['Gender'], siswa['Nilai Biologi']] for nis, siswa in sorted_data.items()]
                                print('Berikut Data Siswa Dengan Nilai Biologi Terbesar Hingga Terkecil\n')
                                print(tabulate(list_siswa, headers=["NIS", "Nama", "Kelas", "Gender", "Nilai Biologi"], tablefmt='fancy_grid'))
                                sub_sorting()
                            elif biologi_urut == '2':
                                sorted_data = dict(sorted(data_siswa.items(), key=lambda x: x[1]['Nilai Biologi']))
                                list_siswa = [[nis, siswa['Nama'], siswa['Kelas'], siswa['Gender'], siswa['Nilai Biologi']] for nis, siswa in sorted_data.items()]
                                print('Berikut Data Siswa Dengan Nilai Biologi Terkecil Hingga Terbesar\n')
                                print(tabulate(list_siswa, headers=["NIS", "Nama", "Kelas", "Gender", "Nilai Biologi"], tablefmt='fancy_grid'))
                                sub_sorting()
                            elif biologi_urut == '3':
                                sorting_back()
                                break
                            else:
                                inputan_tidak_valid()
                                break
                    elif sorting_input == '4':
                        os.system('cls')
                        print('Kembali Ke Report Nilai Siswa')
                        break
                    else:
                        inputan_tidak_valid()
                        continue
            elif menu_read == '4':
                while True:
                    print('='*40)
                    print(f'{"FILTERING":^40}')       
                    print('='*40)
                    filtering_input = input('\n1. Daftar Siswa Remedial MTK\n2. Daftar Siswa Remedial Fisika\n3. Daftar Siswa Remedial Biologi\n4. Kembali Ke Menu Report Nilai Siswa\n\nPilihan Nomor: ')
                    os.system('cls')
                    if filtering_input == '1':
                        data_remed = filter_nilai_mtk(data_siswa)
                        # mencari dari data_siswa yang memiliki nilai mtk dibawah 75
                        print(f'{"Daftar Siswa Yang Mengikut Remedial MTK":^54}')
                        print(tabulate(listing_mtk(), headers=["NIS", "Nama", "Kelas", "Gender", "Nilai MTK"], tablefmt='fancy_grid'))
                        sub_sorting()
                    elif filtering_input == '2':
                        data_remed = filter_nilai_fisika(data_siswa)
                        print(f'{"Daftar Siswa Yang Mengikut Remedial Fisika":^54}')
                        print(tabulate(listing_fisika(), headers=["NIS", "Nama", "Kelas", "Gender", "Nilai Fisika"], tablefmt='fancy_grid'))
                        sub_sorting()
                    elif filtering_input == '3':
                        data_remed = filter_nilai_biologi(data_siswa)
                        print(f'{"Daftar Siswa Yang Mengikut Remedial Biologi":^54}')
                        print(tabulate(listing_biologi(), headers=["NIS", "Nama", "Kelas", "Gender", "Nilai Biologi"], tablefmt='fancy_grid'))
                        sub_sorting()
                    elif filtering_input == '4':
                        os.system('cls')
                        print('Kembali Ke Report Nilai Siswa')
                        break
                    else:
                        inputan_tidak_valid()
                        
            elif menu_read == '5':
                os.system('cls')
                print('KEMBALI KE MENU UTAMA\n')
                break
            elif menu_read == '0':
                exit()
            else:
                inputan_tidak_valid()
                continue
    elif menu_input == '2':
        os.system('cls')
        while True:
            # CREATE
            print('='*30)
            print(f'{"MENU CREATE":^30}')
            print('='*30)
            print(f'\n1. Tambah Data Siswa\n2. Kembali Ke Menu Utama\n\n0. Keluar Dari Program')
            menu_create = input('\n\nSilahkan Pilih Menu: ')
            if menu_create == '1':
                # membuat p.key baru
                new_nis = input('Masukan NIS: ')
                if not new_nis.isdigit():
                    # ketika inputan bukan angka bilangan positif akan salah
                    os.system('cls')
                    print('NIS Harus Berupa Angka Positif\n')
                    continue
                new_nis = int(new_nis)  # Konversi ke integer
                if new_nis in data_siswa:  # Periksa apakah NIS sudah ada
                    os.system('cls')

                    print('NIS Sudah Ada\n')
                    continue
                new_nama = input('Masukan Nama: ')
                if not new_nama.replace(' ','').isalpha():
                    os.system('cls')

                    print('Nama Harus Berupa Huruf\n')
                    continue
                new_nama = new_nama.title()
                new_class = input('Masukan Kelas [Contoh: 12A, 12B, dst]: ')
                if len(new_class) != 3 or not new_class.startswith('12') or new_class.isdigit():  # Periksa format kelas
                    os.system('cls')

                    print('Kelas Harus Terdiri Dari Gabungan 12 dan Huruf (Contoh: 12A, 12B, dst)\n')
                    continue
                new_class = new_class.upper()
                new_gender = input('Masukan Gender [L/P]: ').upper()
                if not new_gender.upper() in ['L', 'P']:  # Periksa gender
                    os.system('cls')

                    print('Gender Hanya Dapat L -> Laki-Laki atau P -> Perempuan\n')
                    continue
                new_nilai_mtk = input('Masukan Nilai Matematika: ')
                if not new_nilai_mtk.isnumeric() or (int(new_nilai_mtk) < 0 or int(new_nilai_mtk) > 100):  # Periksa apakah nilai berupa angka
                    os.system('cls')
                    
                    print('Nilai Harus Berupa Angka dan Pada Rentang 0-100\n')
                    continue
                new_nilai_mtk = int(new_nilai_mtk)  # Konversi ke integer
                new_nilai_fisika = input('Masukan Nilai Fisika: ')
                if not new_nilai_fisika.isnumeric() or (int(new_nilai_fisika) < 0 or int(new_nilai_fisika) > 100):  # Periksa apakah nilai berupa angka
                    os.system('cls')

                    print('Nilai Harus Berupa Angka dan Pada Rentang 0-100\n')
                    continue
                new_nilai_fisika = int(new_nilai_fisika)  # Konversi ke integer
                new_nilai_biologi = input('Masukan Nilai Biologi: ')
                if not new_nilai_biologi.isnumeric() or (int(new_nilai_biologi) < 0 or int(new_nilai_biologi) > 100):  # Periksa apakah nilai berupa angka
                    os.system('cls')

                    print('Nilai Harus Berupa Angka dan Pada Rentang 0-100\n')
                    continue
                new_nilai_biologi = int(new_nilai_biologi)  # Konversi ke integer
                # Tambahkan data siswa baru ke dictionary data_siswa
                print('Berikut adalah data baru yang akan ditambahkan:\n')
                data_create = dict()
                data_create['Nama'] = [new_nama]
                data_create['Kelas'] = [new_class]
                data_create['Gender'] = [new_gender]
                data_create['Nilai MTK'] = [new_nilai_mtk]
                data_create['Nilai Fisika'] = [new_nilai_fisika]
                data_create['Nilai Biologi'] = [new_nilai_biologi]
                print('NIS:',new_nis, data_create)
                data_create_confirm = input('Apakah Data Baru Ingin Disimpan? [Y/N]: ').upper()
                if data_create_confirm == 'N':
                    print('Data Tidak Akan Disimpan\n')
                    continue
                elif data_create_confirm == 'Y':
                    os.system('cls')
                    data_siswa[new_nis] = {'Nama': new_nama, 'Kelas': new_class, 'Gender': new_gender, 'Nilai MTK': new_nilai_mtk, 'Nilai Fisika': new_nilai_fisika, 'Nilai Biologi': new_nilai_biologi}
                    # Membuat ulang list_siswa setelah menambahkan data baru
                    listing()
                    # Cetak tabel siswa setelah menambahkan data baru
                    print(f'Data Sudah Lengkap\nBerikut Data Setelah Ditambahkan NIS: {new_nis}')
                    print(tabulate(listing(), headers=["NIS", "Nama", "Kelas", "Gender", "Nilai MTK", "Nilai Fisika", "Nilai Biologi"], tablefmt='fancy_grid'))
                    sub_sorting()
                else:
                    inputan_tidak_valid()
                    continue
            elif menu_create == "2":
                os.system('cls')
                break
            elif menu_create == "0":
                os.system('cls')
                exit()
            else:
                inputan_tidak_valid()
                continue
    elif menu_input == '3':
        os.system('cls')
        while True:
            print('='*30)
            print(f'{"MENU UPDATE":^30}')
            print('='*30)
            nis_update = input('1. Update Data Siswa\n2. Kembali Ke Menu Utama\n\n0. Keluar Dari Program\nSilahkan Pilih Menu: ')
            if nis_update == '1':
                os.system('cls')
                print(f'{"Berikut Adalah Data Siswa":^90}')
                print()
                print(tabulate(listing(), headers=["NIS", "Nama", "Kelas", "Gender", "Nilai MTK", "Nilai Fisika", "Nilai Biologi"], tablefmt='fancy_grid'))
                change_nis = input('Masukan NIS untuk diupate: ')
                if not change_nis.isdigit():
                    os.system('cls')
                    print('NIS Harus Berupa Angka')
                    continue
                elif int(change_nis) in data_siswa:
                    change_nis = int(change_nis)
                    os.system('cls')
                    change_nis_confirmation = input(f'Ingin Mengubah Data NIS: {change_nis}? [Y/N]: ').upper()
                    if change_nis_confirmation == 'Y':
                        os.system('cls')
                        print('='*30)
                        print(f'{"MERUBAH DATA":^30}')
                        print('='*30)
                        update_apa = input('\n1. Semua Data\n2. NIS\n3. Nama \n4. Kelas\n5. Gender\n6. Nilai MTK\n7. Nilai Fisika\n8. Nilai Biologi\nSilahkan Pilih Menu: ')
                        os.system('cls')
                        if update_apa == '1':

                            new_nama = input('Masukan Nama: ').title()
                            if not new_nama.replace(' ','').isalpha():
                                os.system('cls')

                                print('Nama Harus Berupa Huruf dan Satu Kata\n')
                                continue
                            new_nama = new_nama.title()
                            new_class = input('Masukan Kelas [Contoh: 12A, 12B, dst]: ')
                            if len(new_class) != 3 or not new_class.startswith('12') or new_class.isdigit():  # Periksa format kelas
                                os.system('cls')

                                print('Kelas Harus Terdiri Dari Gabungan 12 dan Huruf (Contoh: 12A, 12B, dst)\n')
                                continue
                            new_class = new_class.upper()
                            new_gender = input('Masukan Gender [L/P]: ').upper()
                            if not new_gender.upper() in ['L', 'P']:  # Periksa gender
                                os.system('cls')

                                print('Gender Hanya Dapat L -> Laki-Laki atau P -> Perempuan\n')
                                continue
                            new_nilai_mtk = input('Masukan Nilai Matematika: ')
                            if not new_nilai_mtk.isnumeric() or (int(new_nilai_mtk) < 0 or int(new_nilai_mtk) > 100):  # Periksa apakah nilai berupa angka
                                os.system('cls')
                                
                                print('Nilai Harus Berupa Angka dan Pada Rentang 0-100\n')
                                continue
                            new_nilai_mtk = int(new_nilai_mtk)  # Konversi ke integer
                            new_nilai_fisika = input('Masukan Nilai Fisika: ')
                            if not new_nilai_fisika.isnumeric() or (int(new_nilai_fisika) < 0 or int(new_nilai_fisika) > 100):  # Periksa apakah nilai berupa angka
                                os.system('cls')

                                print('Nilai Harus Berupa Angka dan Pada Rentang 0-100\n')
                                continue
                            new_nilai_fisika = int(new_nilai_fisika)  # Konversi ke integer
                            new_nilai_biologi = input('Masukan Nilai Biologi: ')
                            if not new_nilai_biologi.isnumeric() or (int(new_nilai_biologi) < 0 or int(new_nilai_biologi) > 100):  # Periksa apakah nilai berupa angka
                                os.system('cls')

                                print('Nilai Harus Berupa Angka dan Pada Rentang 0-100\n')
                                continue
                            new_nilai_biologi = int(new_nilai_biologi)  # Konversi ke integer
                            # Tambahkan data siswa baru ke dictionary data_siswa
                            os.system('cls')
                            print(f'{"Berikut Adalah Data Setelah Diubah":^90}')
                            print()
                            data_create = dict()
                            data_create['Nama'] = [new_nama]
                            data_create['Kelas'] = [new_class]
                            data_create['Gender'] = [new_gender]
                            data_create['Nilai MTK'] = [new_nilai_mtk]
                            data_create['Nilai Fisika'] = [new_nilai_fisika]
                            data_create['Nilai Biologi'] = [new_nilai_biologi]
                            print('NIS:',change_nis, data_create)
                            data_update_confirm = input('\n Apakah Data Akan Disimpan? [Y/N]: ').upper()
                            if data_update_confirm == 'N':
                                os.system('cls')
                                print('Data Tidak Akan Disimpan\n')
                                continue
                            elif data_update_confirm == 'Y':
                                os.system('cls')
                                data_siswa[change_nis] = {'Nama': new_nama, 'Kelas': new_class, 'Gender': new_gender, 'Nilai MTK': new_nilai_mtk, 'Nilai Fisika': new_nilai_fisika, 'Nilai Biologi': new_nilai_biologi}
                                # Membuat ulang list_siswa setelah menambahkan data baru
                                listing()
                                # Cetak tabel siswa setelah menambahkan data baru
                                print(f'Data Sudah Lengkap\nBerikut Data Setelah NIS: {change_nis} di Update:')
                                print(tabulate(listing(), headers=["NIS", "Nama", "Kelas", "Gender", "Nilai MTK", "Nilai Fisika", "Nilai Biologi"], tablefmt='fancy_grid'))
                                print()
                                menu_back = input('1. Kembali Ke Menu Update\n2. Kembali ke Menu Utama\n\n0. Keluar Dari Program\n\nSilahkan Pilih Menu: ')
                                if menu_back == '1':
                                    os.system('cls')
                                    continue
                                elif menu_back == '2':
                                    os.system('cls')
                                    break
                                elif menu_back == '0':
                                    os.system('cls')
                                    exit()
                                else:
                                    inputan_tidak_valid()
                                    continue
                            else:
                                inputan_tidak_valid()
                        elif update_apa == '2':
                            change_nis_replace = input('Masukan NIS Baru: ')
                            if not change_nis_replace.isdigit():
                                # yang bukan bilangan angka positif akan salah
                                print('NIS Harus Berupa Angka')
                            elif change_nis_replace.isdigit():
                                change_nis_replace = int(change_nis_replace)
                                if not change_nis_replace in data_siswa: # dicek apakah NIS sudah ada atau belum
                                    nis_update_confirm = input(f'Apakah Yakin Mengganti {change_nis} menjadi --> {change_nis_replace} [Y/N]: ').upper() #konfirmasi update
                                    if change_nis_confirmation == 'Y':
                                        data_dummy = data_siswa[change_nis] #membuat data_dummy dengan mengambil segala value pada nis yang diganti
                                        del data_siswa[change_nis]
                                        data_siswa[change_nis_replace] = data_dummy #memasukan p.key baru menggunakan value dari data dummy
                                        listing() # melakukan listing lagi untuk memperbarui tampilan tabulate
                                        os.system('cls')
                                        print('Data Telah Terganti')
                                    elif change_nis_confirmation == 'N':
                                        os.system('cls')
                                        print('Data Tidak Diubah')
                                        continue
                                    else:
                                        inputan_tidak_valid()
                                        continue
                                elif change_nis_replace in data_siswa:
                                    print('NIS Sudah Ada, Masukan NIS Lain!') #kondisi ketika nis sudah ada
                                    continue
                                else:
                                    inputan_tidak_valid()
                            else:
                                inputan_tidak_valid()
                        elif update_apa == '3': # Update Nama
                            nama_update = input('Masukan Nama Baru: ').title()
                            if not nama_update.replace(' ','').isalpha():
                                os.system('cls')
                                print('Nama Harus Berupa Alpabet')
                                continue
                            
                            data_siswa[change_nis]['Nama'] = nama_update #mengubah nama dengan menggunakan p.key -> change_nis dan memanggil key dalam key yaitu nilai, dan valuenya diubah sesuai inputan
                            listing()
                            os.system('cls')
                            print('Nama Telah Terganti')
                        elif update_apa == '4': # Update Kelas
                            kelas_update = input('Masukan Kelas Baru [Contoh: 12A, 12B, dst]: ').upper()
                            if len(kelas_update) != 3 or not kelas_update.startswith('12') or kelas_update.isnumeric():  # Periksa format kelas
                                os.system('cls')
                                print('Kelas Harus Terdiri Dari Gabungan 12 dan Huruf (Contoh: 12A, 12B, dst)\n')
                                continue
                            data_siswa[change_nis]['Kelas'] = kelas_update
                            listing()
                            os.system('cls')
                            print('Kelas Telah Terganti')
                        elif update_apa == '5': # Update Gender
                            gender_update = input('Masukan Gender [L/P]: ').upper()
                            if not gender_update.upper() in ['L', 'P']:  # Periksa gender
                                os.system('cls')
                                print('Gender Hanya Dapat L -> Laki-Laki atau P -> Perempuan\n')
                                continue
                            data_siswa[change_nis]['Gender'] = gender_update
                        elif update_apa == '6': # Update Nilai MTK
                            nilai_mtk_update = input('Masukan Nilai Matematika: ')
                            if not nilai_mtk_update.isnumeric() or (int(nilai_mtk_update) < 0 or int(nilai_mtk_update) > 100):  # Periksa apakah nilai berupa angka
                                os.system('cls')
                                print('Nilai Harus Berupa Angka dan Pada Rentang 0-100\n')
                                continue
                            nilai_mtk_update = int(nilai_mtk_update)  # Konversi ke integer
                            data_siswa[change_nis]['Nilai MTK'] = nilai_mtk_update
                        elif update_apa == '7': # Update Nilai Fisika
                            nilai_fisika_update = input('Masukan Nilai Fisika: ')
                            if not nilai_fisika_update.isnumeric() or (int(nilai_fisika_update) < 0 or int(nilai_fisika_update) > 100):  # Periksa apakah nilai berupa angka
                                os.system('cls')
                                print('Nilai Harus Berupa Angka dan Pada Rentang 0-100\n')
                                continue
                            nilai_fisika_update = int(nilai_fisika_update)  # Konversi ke integer
                            data_siswa[change_nis]['Nilai Fisika'] = nilai_fisika_update
                        elif update_apa == '8': # Update Nilai Biologi
                            nilai_biologi_update = input('Masukan Nilai Biologi: ')
                            if not nilai_biologi_update.isnumeric() or (int(nilai_biologi_update) < 0 or int(nilai_biologi_update) > 100):  # Periksa apakah nilai berupa angka
                                os.system('cls')
                                print('Nilai Harus Berupa Angka dan Pada Rentang 0-100\n')
                                continue
                            nilai_biologi_update = int(nilai_biologi_update)  # Konversi ke integer
                            data_siswa[change_nis]['Nilai Biologi'] = nilai_biologi_update
                        else:
                            inputan_tidak_valid()
                            continue
                    else:
                        inputan_tidak_valid()
                        continue
                else:
                    os.system('cls')
                    print(f'NIS: {change_nis} Tidak Tersedia\n')
                    continue   
            elif nis_update == '2':
                os.system('cls')
                break
            elif nis_update == '0':
                os.system('cls')
                exit()
            else:
                inputan_tidak_valid()
                continue
    elif menu_input == '4':
        while True:
            print('='*30)
            print(f'{"MENU DELETE":^30}')
            print('='*30)
            menu_delete = input('1. Ingin Menghapus Data?\n2. Kembali Ke Menu Utama\n3. Hapus Semua Data\n\n0. Keluar Dari Program\nSilahkan Pilih Menu: ')
            os.system('cls')
            if menu_delete == '1':
                print(f'{"Berikut Adalah Data Siswa":^90}')
                print(tabulate(listing(), headers=["NIS", "Nama", "Kelas", "Gender", "Nilai MTK", "Nilai Fisika", "Nilai Biologi"], tablefmt='fancy_grid'))
                pilihan_delete = input('\nNIS Mana Yang Ingin Dihapus: ')
                os.system('cls')
                if not pilihan_delete.isnumeric():
                    inputan_tidak_valid()
                    continue
                if int(pilihan_delete) not in(data_siswa):
                    os.system('cls')
                    print('NIS Tidak ada')
                    continue
                delete_dummy = data_siswa.copy() #membuat variabel dummy untuk membuat tampilan ketika data telah dihapus
                del delete_dummy[int(pilihan_delete)] # delete var dummy sesuai dengan inputan primary key, akan hapus semua data dari p.key
                print(f'(Berikut Adalah Data Setelah NIS: {pilihan_delete} Dihapus') #tampilan ketika dihapus secara tabulate
                list_dummy = [[nis, siswa['Nama'], siswa['Kelas'], siswa['Gender'], siswa['Nilai MTK'], siswa['Nilai Fisika'], siswa['Nilai Biologi']] for nis, siswa in delete_dummy.items()]
                print(tabulate(list_dummy, headers=["NIS", "Nama", "Kelas", "Gender", "Nilai MTK", "Nilai Fisika", "Nilai Biologi"], tablefmt='fancy_grid'))
                delete_confirm = input('\nApakah Data Akan Dihapus? [Y//N]').upper()
                if delete_confirm == 'N':
                    os.system('cls')
                    print('Data Tidak Dihapus')
                    continue
                elif delete_confirm == 'Y':
                    os.system('cls')
                    data_siswa = delete_dummy #replace data_siswa sesuai dengan delete_dummy -> karena data telah dikonfirmasi
                    listing()
                    print(f'{"Data Telah Dihapus":^30}')
                    break
                else:
                    inputan_tidak_valid()
                    continue
            elif menu_delete == '2':
                os.system('cls')
                break
            elif menu_delete == '3':
                clear_confirm = input('Apakah Yakin Ingin Menghapus Semua Data? [Y/N]: ').upper()
                if clear_confirm == 'Y':
                    os.system('cls')
                    data_siswa.clear()
                    listing()
                    print('Semua Data Dihapus')
                elif clear_confirm == 'N':
                    os.system('cls')
                    print('Data Tidak Jadi Dihapus')
                    continue
                else:
                    inputan_tidak_valid()
                    continue
            elif menu_delete == '0':
                exit()
            else:
                os.system('cls')
                inputan_tidak_valid()
                continue
    elif menu_input == '5':
        while True:
            print('='*30)
            print(f'{"MENU ROLLBACK":^30}')
            print('='*30)
            input_recovery = input('1. Rollback Data\n2. Kembali Ke Menu Utama\n\n0. Keluar Dari Program: ')
            if input_recovery == '1':
                rollback_confirm = input('Apakah Yakin Untuk Melakukan Rollback Data? [Y/N]: ').upper()
                if rollback_confirm == 'Y':
                    data_recovery(backup_data)
                    listing()
                    os.system('cls')
                    print(f'{"Data Dikembalikan Seperti Semula!":^30}')
                elif rollback_confirm == 'N':
                    os.system('cls')
                    print('Tidak Dilakukan Rollback')
                    continue
                else:
                    inputan_tidak_valid()
                    continue
            elif input_recovery == '2':
                os.system('cls')
                break
            elif input_recovery == '0':
                os.system('cls')
                exit()
            else:
                os.system('cls')
                inputan_tidak_valid()
    elif menu_input == '0':
        break
    else:
        print(f'\n{"Hanya Dapat Memilih Nomor Yang Ada Pada Menu":^60}\n')

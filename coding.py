def menu() :
    import os
    os.system("CLS")
    print("     Selamat Datang Di Perpustakaan Umum")
    print("Berikut Adalah Riwayat Peminjaman Buku Anda")
    print("             \nDaftar Menu: ")
    print("[1] Melihat Daftar Riwayat Peminjaman")
    print("[2] Menambah Riwayat Peminjaman Baru")
    print("[3] Mencari Riwayat Peminjaman")
    print("[4] Memperbarui Riwayat Peminjaman")
    print("[5] Menghapus Riwayat Peminjaman")
    print("[6] Keluar dari Program")
    pil = int(input("Masukkan No Menu yang Anda Pilih : " ))
    pilihmenu(pil)

def pilihmenu(p) :
    if p == 1:
        lihatdata()
    elif p == 2:
        tambahdata()
    elif p == 3:
        caridata()
    elif p == 4:
        ubahdata()
    elif p == 5:
        hapusdata()
    elif p == 6:
        print("Anda telah keluar dari program.")
        print("Terima kasih atas kunjungan Anda.")
#------------------------------------------------------------------------------
def lihatdata():
    import os
    os.system("CLS")
    print("\nAnda Berada Pada Menu Menampilkan Data Buku")
    bukadata = open("data/databuku.txt","r")
    isi = bukadata.readlines()
    isi.sort()
    if len(isi) == 0:
        print("\nData buku Anda masih KOSONG.") 
        print("\nTekan [ENTER] untuk melanjutkan!")
        input()
        menu()
    else :
        i = 1 
        for data_buku in isi:
            pecah = data_buku.split(",")
            print("\n" + str(i) + ".",end=" ")
            print(pecah[0]+" , "+ pecah[1]+" , "+ pecah[2],end=" ")
            i += 1

        print("\nTekan [ENTER] untuk kembali ke menu!")
        bukadata.close()
        input()
        menu()
#------------------------------------------------------------------------------
def tambahdata() :
    import os
    os.system("CLS")
    print("Anda Berada Pada Menu Menambah Data Buku Pinjaman")
    print("Masukkan Judul Buku Secara Detail. (Kapital!)")
    bukadata = open("data/databuku.txt","a")
    judulbuku = input("\nMasukkan Judul Buku            : ")
    penulis = input("Masukkan Nama Penulis          : ")
    tanggal = input("Masukkan Tanggal Peminjaman    : ")
    bukadata.writelines([judulbuku +", " + penulis + ", " + tanggal + "\n"])
    bukadata.close()

    print("\nIngin meminjam buku lagi? (Ya/Tidak)",end="")
    tmbhdata = input(" : ")
    if tmbhdata == "ya" or tmbhdata == "Ya":
        tambahdata()
    else :
        menu()
#------------------------------------------------------------------------------
def caridata() :
    import os
    os.system("CLS")
    print("\nAnda Berada Pada Menu Pencarian Buku Pinjaman")
    caribuku = str(input("\nCari Buku Berdasarkan (Judul/Penulis) : "))
    counter = 0
    number = 1
    if caribuku == "Judul" or caribuku == "judul":
        print("Ketik judul secara DETAIL!")
        keyword = input("Masukkan Judul Buku yang Anda Cari : ")
        bukadata = open("data/databuku.txt")
        for search_data in bukadata:
            if search_data.startswith(keyword):
                pecah = search_data.split(",")
                print("\nJudul Buku           : " + pecah [0])
                print("Penulis              : " + pecah [1])
                print("Tanggal Peminjaman   : " + pecah [2])
                print("Tekan [ENTER] untuk melanjutkan!")
                input()
        if counter == 0:
            print("\nTidak ditemukan data buku dengan Judul :" + keyword)
        bukadata.close()    
    else :
        print("Ketik nama penulis secara DETAIL!")
        keyword2 = input("\nMasukkan Nama Penulis : ")
        bukadata = open("data/databuku.txt")
        bukabuku = bukadata.readlines()
        bukabuku.sort()
        for i in bukabuku:
            x = i.strip()
            y = x.split(",")
            z = y[0] + " " + y[1] + " " + y[2] + " "
            if keyword2 in z:
                print("Judul Buku           : " + y[0])
                print("Penulis              : " + y[1])
                print("Tanggal Peminjaman   : " + y[2] + "\n")
        if counter == 0:
            print("\nTidak ditemukan data buku dengan Penulis : " + keyword2)
        bukadata.close()

    print("\nIngin mencari buku lagi? (Ya/Tidak)",end="")
    crdata = input(" : ")
    if crdata == "ya" or crdata == "Ya":
        caridata()
    else :
        menu()
#------------------------------------------------------------------------------    
def ubahdata():
    import os
    os.system("CLS")
    print("\nAnda Berada Pada Menu Untuk Memperbarui Data Buku Pinjaman")
    delete = input("Apakah Anda Yakin Akan Mengganti Data Riwayat Peminjaman? (Ya/Tidak) : ")

    if delete == "ya" or delete == "Ya":
        bukadata = open("data/databuku.txt")
        output = []
        print("\n")
        data = input("Masukkan Judul Buku yang Akan Ganti! : ")
        for base in bukadata:
            if not base.startswith(data):
                output.append(base)
        bukadata.close()
        bukadata = open("data/databuku.txt","w")
        bukadata.writelines(output)
        
    print("\nMasukkan data baru!")   
    bukadata = open("data/databuku.txt","a")
    judulbuku = input("\nMasukkan Judul Buku            : ")
    penulis = input("Masukkan Nama Penulis          : ")
    tanggal = input("Masukkan Tanggal Peminjaman    : ")
    bukadata.writelines([judulbuku +", " + penulis + ", " + tanggal + "\n"])
    bukadata.close()

    print("\nIngin memperbarui riwayat peminjaman buku lagi? (Ya/Tidak)",end="")
    updatedata = input(" : ")
    if updatedata == "ya" or updatedata == "Ya":
        ubahdata()
    else :
        menu()
#------------------------------------------------------------------------------   
def hapusdata() :
    import os
    os.system("CLS")
    print("\nAnda Berada Pada Menu Menghapus Data Buku Pinjaman")
    print("\nBerikut Data Buku yang Telah Dipinjam :")
    bukadata = open("data/databuku.txt","r")
    isi = bukadata.readlines()
    isi.sort()
    if len(isi) == 0 :
        print("Data buku Anda masih KOSONG") 
        print("\nTekan [ENTER] untuk melanjutkan!")
        input()
        menu()
    else :
        i = 1 
        for data_buku in isi :
            pecah = data_buku.split(",")
            print("\n" + str(i) + ".",end=" ")
            print(pecah[0]+" , "+ pecah[1]+" , "+ pecah[2],end=" ")
            i += 1

    print("\n")
    print("Data yang Telah Dihapus TIDAK DAPAT Dikembalikan Lagi")
    delete = input("Apakah Anda Yakin Akan Menghapus Riwayat Peminjaman? (Ya/Tidak) : ")

    if delete == "ya" or delete == "Ya":
        bukadata = open("data/databuku.txt")
        output = []
        print("\n")
        data = input("Masukkan Judul Buku yang Akan Dihapus! : ")
        for base in bukadata:
            if not base.startswith(data):
                output.append(base)
        
        bukadata.close()
        bukadata = open("data/databuku.txt","w")
        bukadata.writelines(output)
        bukadata.close()

    print("\nIngin menghapus buku lagi? (Ya/Tidak)",end="")
    deldata = input(" : ")
    if deldata == "ya" or deldata == "Ya":
        hapusdata()
    else :
        menu()   
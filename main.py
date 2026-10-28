import sys
from src.input_data import baca_data_dari_file, input_data_manual
from src.proses import ringkasan, hitung_rata_rata
from src.output import tampilkan_ringkasan, simpan_hasil_ke_file

def jalankan_test_manual():
    """
    Uji coba internal fungsi menggunakan assert statement.
    """
    assert hitung_rata_rata([70, 80, 90]) == 80.0
    assert hitung_rata_rata([]) == 0.0
    print("Assertion tests berhasil dijalankan (PASS).")

def main():
    jalankan_test_manual()
    
    print("\n==========================================")
    print("  APLIKASI ANALISIS NILAI SISWA (MATEMATIKA)")
    print("==========================================")
    print("1. Baca data dari file (data/contoh_data.txt)")
    print("2. Input data siswa secara manual")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1/2/3): ").strip()
    data_siswa = []

    if pilihan == '1':
        path = "data/contoh_data.txt"
        try:
            data_siswa = baca_data_dari_file(path)
            print(f"\nBerhasil membaca {len(data_siswa)} data dari {path}.")
        except FileNotFoundError as e:
            print(f"\n[Error] {e}")
            return
    elif pilihan == '2':
        data_siswa = input_data_manual()
    elif pilihan == '3':
        print("Program selesai.")
        sys.exit()
    else:
        print("Pilihan tidak valid.")
        return

    if not data_siswa:
        print("Tidak ada data yang dapat diproses.")
        return

    hasil = ringkasan(data_siswa)
    tampilkan_ringkasan(hasil, data_siswa)
    
    simpan = input("Apakah ingin menyimpan hasil ke file? (y/n): ").strip().lower()
    if simpan == 'y':
        simpan_hasil_ke_file(hasil)

if __name__ == "__main__":
    main()
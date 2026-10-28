import os

def tampilkan_ringkasan(hasil_ringkasan, data_siswa=None):
    """
    Menampilkan ringkasan statistik ke terminal.
    """
    print("\n==========================================")
    print("         RINGKASAN ANALISIS NILAI         ")
    print("==========================================")
    print(f"Jumlah Siswa       : {hasil_ringkasan['jumlah']}")
    print(f"Rata-rata Nilai    : {hasil_ringkasan['rata_rata']:.2f}")
    print(f"Nilai Minimum      : {hasil_ringkasan['minimum']}")
    print(f"Nilai Maksimum     : {hasil_ringkasan['maksimum']}")
    print(f"Jumlah Lulus (>=60): {hasil_ringkasan['lulus']}")
    print(f"Tidak Lulus        : {hasil_ringkasan['tidak_lulus']}")
    print("==========================================")

    if data_siswa:
        print("\nDetail Data Siswa:")
        for idx, siswa in enumerate(data_siswa, 1):
            status = "LULUS" if siswa["nilai"] >= 60 else "TIDAK LULUS"
            print(f"{idx}. {siswa['nama']} - Nilai: {siswa['nilai']} ({status})")
        print("==========================================\n")

def simpan_hasil_ke_file(hasil_ringkasan, filepath="data/hasil_analisis.txt"):
    """
    Menyimpan hasil analisis ke file teks.
    """
    folder = os.path.dirname(filepath)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
        
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write("=== HASIL ANALISIS NILAI ===\n")
        f.write(f"Jumlah Siswa       : {hasil_ringkasan['jumlah']}\n")
        f.write(f"Rata-rata          : {hasil_ringkasan['rata_rata']:.2f}\n")
        f.write(f"Nilai Minimum      : {hasil_ringkasan['minimum']}\n")
        f.write(f"Nilai Maksimum     : {hasil_ringkasan['maksimum']}\n")
        f.write(f"Lulus              : {hasil_ringkasan['lulus']}\n")
        f.write(f"Tidak Lulus        : {hasil_ringkasan['tidak_lulus']}\n")
        f.write("============================\n\n")
    print(f"Hasil analisis berhasil disimpan ke: {filepath}")
import os

def baca_data_dari_file(filepath):
    """
    Membaca data nilai siswa dari file teks.
    Format baris pada file: Nama,Nilai
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File data tidak ditemukan di: {filepath}")
    
    data_siswa = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 2:
                continue
            nama, nilai_str = parts[0].strip(), parts[1].strip()
            try:
                nilai = float(nilai_str)
                data_siswa.append({"nama": nama, "nilai": nilai})
            except ValueError:
                continue
    return data_siswa

def input_data_manual():
    """
    Mengambil input nilai siswa secara manual melalui terminal dengan validasi.
    """
    data_siswa = []
    print("\n--- Input Data Siswa Manual ---")
    while True:
        nama = input("Masukkan nama siswa (atau ketik 'selesai' untuk mengakhiri): ").strip()
        if nama.lower() == 'selesai':
            break
        if not nama:
            print("Nama tidak boleh kosong.")
            continue
        
        while True:
            try:
                nilai_input = input(f"Masukkan nilai untuk {nama} (0-100): ").strip()
                nilai = float(nilai_input)
                if 0 <= nilai <= 100:
                    data_siswa.append({"nama": nama, "nilai": nilai})
                    break
                else:
                    print("Nilai harus berada dalam rentang 0 - 100.")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka yang valid.")
    return data_siswa
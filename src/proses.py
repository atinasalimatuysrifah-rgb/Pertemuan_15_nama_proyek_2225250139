BATAS_LULUS = 60.0

def hitung_rata_rata(nilai):
    """
    Mengembalikan rata-rata list numerik.
    Jika data kosong, fungsi mengembalikan 0.
    """
    if not nilai:
        return 0.0
    return sum(nilai) / len(nilai)

def status_lulus(nilai, batas=BATAS_LULUS):
    """
    Mengembalikan list nilai yang memenuhi batas kelulusan.
    """
    return [x for x in nilai if x >= batas]

def ringkasan(data_siswa, batas=BATAS_LULUS):
    """
    Menghasilkan dictionary ringkasan analisis statistik nilai.
    """
    if not data_siswa:
        return {
            "jumlah": 0,
            "rata_rata": 0.0,
            "minimum": None,
            "maksimum": None,
            "lulus": 0,
            "tidak_lulus": 0
        }
    
    daftar_nilai = [siswa["nilai"] for siswa in data_siswa]
    lulus_list = status_lulus(daftar_nilai, batas)
    
    return {
        "jumlah": len(daftar_nilai),
        "rata_rata": hitung_rata_rata(daftar_nilai),
        "minimum": min(daftar_nilai),
        "maksimum": max(daftar_nilai),
        "lulus": len(lulus_list),
        "tidak_lulus": len(daftar_nilai) - len(lulus_list)
    }
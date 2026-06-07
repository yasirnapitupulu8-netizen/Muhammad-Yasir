KAPASITAS_MAKSIMAL = 500
AMBANG_PENUH = 400
AMBANG_AMAN = 100

MINIMAL_PERISHABLE = 150
MINIMAL_REGULER = 50

def hitung_total_stok(stok_saat_ini, jumlah_masuk):
    """Menghitung total akumulasi stok barang di gudang."""
    return stok_saat_ini + jumlah_masuk

def evaluasi_status_kapasitas(total_stok):
    """Menentukan kategori kondisi kapasitas tampung gudang."""
    if total_stok > KAPASITAS_MAKSIMAL:
        return "OVERFLOW"
    if total_stok >= AMBANG_PENUH:
        return "PENUH"
    if total_stok >= AMBANG_AMAN:
        return "AMAN"
    return "KRITIS"

def periksa_kebutuhan_restock(total_stok, jenis_barang):
    """Memeriksa apakah stok barang sudah menyentuh batas minimum untuk pengadaan ulang."""
    ambang_batas = MINIMAL_PERISHABLE if jenis_barang.upper() == "PERISHABLE" else MINIMAL_REGULER
    return total_stok < ambang_batas

def cetak_laporan_gudang(total_stok, status, butuh_restock):
    """Menampilkan laporan kondisi manajemen gudang terupdate ke konsol."""
    print("\n" + "=== STATUS MANAJEMEN GUDANG ===")
    print(f"Total Stok Akhir    : {total_stok} unit")
    print(f"Status Kapasitas    : {status}")
    print(f"Rekomendasi Restock : {'YA, SEGERA BELI' if butuh_restock else 'TIDAK PERLU'}")
    print("===============================")

def cek_inventaris_gudang(stok_saat_ini, jumlah_masuk, jenis_barang):
    """Fungsi utama untuk mengontrol alur proses manajemen inventaris."""
    total_stok = hitung_total_stok(stok_saat_ini, jumlah_masuk)
    status_kapasitas = evaluasi_status_kapasitas(total_stok)
    perlu_restock = periksa_kebutuhan_restock(total_stok, jenis_barang)
    
    cetak_laporan_gudang(total_stok, status_kapasitas, perlu_restock)
    return total_stok

if __name__ == "__main__":
    cek_inventaris_gudang(stok_saat_ini=350, jumlah_masuk=80, jenis_barang="PERISHABLE")
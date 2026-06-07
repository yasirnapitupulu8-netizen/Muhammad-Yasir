KAPASITAS_MAKSIMAL = 500
AMBANG_PENUH = 400
AMBANG_AMAN = 100

MINIMAL_PERISHABLE = 150
MINIMAL_REGULER = 50

def cek_inventaris_gudang(stok_saat_ini, jumlah_masuk, jenis_barang):
    total_stok = stok_saat_ini + jumlah_masuk
    
    # Mengganti angka mentah dengan konstanta deskriptif
    if total_stok > KAPASITAS_MAKSIMAL:
        status_kapasitas = "OVERFLOW"
    elif total_stok >= AMBANG_PENUH:
        status_kapasitas = "PENUH"
    elif total_stok >= AMBANG_AMAN:
        status_kapasitas = "AMAN"
    else:
        status_kapasitas = "KRITIS"
        
    perlu_restock = False
    if jenis_barang == "PERISHABLE":
        if total_stok < MINIMAL_PERISHABLE:
            perlu_restock = True
    else:
        if total_stok < MINIMAL_REGULER:
            perlu_restock = True
            
    print("=== STATUS MANAJEMEN GUDANG ===")
    print(f"Total Stok Akhir: {total_stok}")
    print(f"Status Kapasitas: {status_kapasitas}")
    print(f"Rekomendasi Restock: {'YA' if perlu_restock else 'TIDAK'}")
    print("===============================")
    return total_stok

cek_inventaris_gudang(350, 80, "PERISHABLE")
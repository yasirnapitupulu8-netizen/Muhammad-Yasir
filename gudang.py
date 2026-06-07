def cek_inventaris_gudang(stok_saat_ini, jumlah_masuk, jenis_barang):
    total_stok = stok_saat_ini + jumlah_masuk
    
    status_kapasitas = ""
    if total_stok > 500:
        status_kapasitas = "OVERFLOW"
    elif total_stok >= 400:
        status_kapasitas = "PENUH"
    elif total_stok >= 100:
        status_kapasitas = "AMAN"
    else:
        status_kapasitas = "KRITIS"
        
    perlu_restock = False
    if jenis_barang == "PERISHABLE":
        if total_stok < 150:
            perlu_restock = True
    else:
        if total_stok < 50:
            perlu_restock = True
            
    print("=== STATUS MANAJEMEN GUDANG ===")
    print(f"Total Stok Akhir: {total_stok}")
    print(f"Status Kapasitas: {status_kapasitas}")
    print(f"Rekomendasi Restock: {'YA' if perlu_restock else 'TIDAK'}")
    print("===============================")
    return total_stok

cek_inventaris_gudang(350, 80, "PERISHABLE")
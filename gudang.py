def CekGudang(stok_skrg, item_masuk, jenis):
    tot = stok_skrg + item_masuk
    

    st = ""
    if tot > 500:
        st = "OVERFLOW"
    elif tot >= 400:
        st = "PENUH"
    elif tot >= 100:
        st = "AMAN"
    else:
        st = "KRITIS"
        
    butuh_beli = False
    if jenis == "PERISHABLE":
        if tot < 150:
            butuh_beli = True
    else:
        if tot < 50:
            butuh_beli = True
            
    print("=== STATUS MANAJEMEN GUDANG ===")
    print(f"Total Stok Akhir: {tot}")
    print(f"Status Kapasitas: {st}")
    print(f"Rekomendasi Restock: {'YA' if butuh_beli else 'TIDAK'}")
    print("===============================")
    return tot

CekGudang(350, 80, "PERISHABLE")
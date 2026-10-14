from produk import produk

jumlah_produk = int(input('masukkan jumlah : '))
total_seluruh = 0

for i in range(jumlah_produk):
    print(f'\nProduk ke-{i+1}')
    nama = input('masukkan Nama Barang : ')
    harga = float(input('masukkan Harga Barang : '))
    jumlah = int(input('masukkan Jumlah Barang : '))

    produks = produk(nama, harga)

    produks.tampilkan_info()
    total_per_item = produks.hitung_total(jumlah)
    print(f"Total harga {produks.nama} ({jumlah} buah): Rp{total_per_item}")

    total_seluruh += total_per_item

diskon = produks.hitung_diskon(total_seluruh)
total_bayar = total_seluruh - diskon

print("\n=== HASIL PEMBELIAN ===")
print(f"Total Pembelian: Rp{int(total_seluruh)}")
print(f"Diskon 5% : Rp{int(diskon)}")
print(f"Total Bayar : Rp{int(total_bayar)}")
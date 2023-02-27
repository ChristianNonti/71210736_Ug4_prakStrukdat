import json

jumlah = int(input("Masukkan jumlah barang = "))
daftar = []

for i in range(jumlah):
    nama_barang = input(f"Nama barang {i+1} = ")
    harga_barang = int(input(f"Harga barang {i+1} = "))
    daftar.append({'nama': nama_barang, 'harga': harga_barang})
    
total_harga = sum([barang['harga'] for barang in daftar])
data = {'total': total_harga, 'barang': daftar}
with open('data_barang.json', 'w') as f:
    json.dump(data, f, indent=4)
print("Data barang berhasil disimpan ke dalam file JSON.")
# 1. 
print("=== Variabel dan Tipe Data ===")
nilai_int = 25              
nilai_float = 12.75         
teks = "Hello everyone!"    
daftar = [1, 2, 3, 4, 5]    

print("Tipe data nilai_int:", type(nilai_int))
print("Tipe data nilai_float:", type(nilai_float))
print("Tipe data teks:", type(teks))
print("Tipe data daftar:", type(daftar))

# 2.
print("\n=== List dan Manipulasi ===")
belanja = ["beras", "minyak", "telur"]

def tambah_item(item):
    belanja.append(item)

tambah_item("gula")
tambah_item("kopi")

for item in belanja:
    print(item)

# 3. 
print("\n=== Dictionary ===")
harga_belanja = {
    "beras": 12000,
    "minyak": 17000,
    "telur": 24000,
    "gula": 15000,
    "kopi": 20000
}

for barang, harga in harga_belanja.items():
    print(f"{barang}: Rp{harga}")

total = sum(harga_belanja.values())
print(f"Total harga belanja: Rp{total}")

# 4. 
print("\n=== Fungsi Luas Lingkaran ===")
import math

def hitung_lingkaran(r):
    luas = math.pi * r**2
    keliling = 2 * math.pi * r
    return luas, keliling

jari2 = 7
luas, keliling = hitung_lingkaran(jari2)
print(f"Luas lingkaran (r={jari2}) = {luas:.2f}")
print(f"Keliling lingkaran (r={jari2}) = {keliling:.2f}")

# 5. 
print("\n=== Percabangan Usia ===")
usia = int(input("Masukkan usia: "))

if 0 <= usia <= 13:
    print("Anak")
elif 14 <= usia <= 24:
    print("Remaja")
elif 25 <= usia <= 49:
    print("Dewasa")
elif usia > 50:
    print("Lansia")
else:
    print("Usia tidak valid")
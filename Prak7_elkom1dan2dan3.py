

print("@@@@ @@@@ @@@@ @@@@@")
print("   @ @    @      @")
print("   @ @@@@ @@@@   @")
print("@  @ @    @      @")
print("@@@@ @@@@ @@@@   @")

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

bilangan = int(input("Nilai: "))

hasil_faktorial = faktorial(bilangan)
print(f"Faktorial dari {bilangan} adalah {hasil_faktorial}")

print("@@@@ @@@@ @@@@ @@@@@")
print("   @ @    @      @")
print("   @ @@@@ @@@@   @")
print("@  @ @    @      @")
print("@@@@ @@@@ @@@@   @")

def hitung_vokal_dan_konsonan(kalimat):
    vokal = 0
    konsonan = 0
    for huruf in kalimat:
        huruf = huruf.lower()
        if huruf in 'aeiou':
            vokal += 1
        elif huruf.isalpha():
            konsonan += 1

    return vokal, konsonan

kalimat = input("Masukkan sesuatu: ")

jml_vokal, jml_konsonan = hitung_vokal_dan_konsonan(kalimat)
print(f"Jumlah huruf Vokal: {jml_vokal}")
print(f"Jumlah huruf konsonan: {jml_konsonan}")

def pangkat_kubik(angka):
    return angka ** 3

def cek_pembagian_tiga(angka):
    if angka % 3 == 0:
        return pangkat_kubik(angka)
    else:
        return "False"

# Meminta input dari pengguna
angka = int(input("Masukkan nilai: "))

# Memanggil fungsi cek_pembagian_tiga dan menampilkan hasilnya
hasil = cek_pembagian_tiga(angka)

if hasil != "False":
    print(f"Hasilnya adalah {hasil}")
else:
    print(hasil)

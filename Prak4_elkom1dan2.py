print('@@@@ @@@@ @@@@ @@@@@')
print('   @ @    @      @')
print('   @ @@@@ @@@@   @')
print('@  @ @    @      @')
print('@@@@ @@@@ @@@@   @')

def desimal_ke_biner(angka):
    return bin(angka).replace("0b", "")

def biner_ke_desimal(biner):
    return int(biner, 2)

while True:
    print("- - - -PROGRAM KONVERSI BILANGAN- - - -")
    print("1 -> Angka ke Biner")
    print("2 -> Biner ke Angka")
    print("3 -> Exit")

    pilihan = int(input("Masukkan Pilihan Anda-> "))

    if pilihan == 1:
        angka = int(input("Masukkan Angka angka: "))
        hasil_biner = desimal_ke_biner(angka)
        print(f"Angka {angka} dalam biner adalah {hasil_biner}")
    elif pilihan == 2:
        biner = input("Masukkan Biner: ")
        hasil_desimal = biner_ke_desimal(biner)
        print(f"Biner {biner} dalam desimal adalah {hasil_desimal}")
    elif pilihan == 3:
        print("Terimakasih!!!!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")

print('@@@@ @@@@ @@@@ @@@@@')
print('   @ @    @      @')
print('   @ @@@@ @@@@   @')
print('@  @ @    @      @')
print('@@@@ @@@@ @@@@   @')

def cek_angka_genap(angka):
    return angka % 2 == 0

# Meminta pengguna memasukkan list angka
angka_list = input("Masukkan List Angka (integer) -> ")
angka_list = [int(angka) for angka in angka_list]

# Memeriksa dan mencetak angka genap
angka_genap = [angka for angka in angka_list if cek_angka_genap(angka)]

if angka_genap:
    print("List memiliki angka genap")
else:
    print("List tidak memiliki angka genap.")



print('@@@@ @@@@ @@@@ @@@@@')
print('   @ @    @      @')
print('   @ @@@@ @@@@   @')
print('@  @ @    @      @')
print('@@@@ @@@@ @@@@   @')

def cek_angka_genap(angka):
    return angka % 2 == 0

# Meminta pengguna memasukkan list angka
angka_list = input("Masukkan List Angka (integer) -> ")
angka_list = [int(angka) for angka in angka_list]

# Memeriksa dan mencetak angka genap
angka_genap = [angka for angka in angka_list if cek_angka_genap(angka)]

if angka_genap:
    print("List memiliki angka genap:", angka_genap)
else:
    print("List tidak memiliki angka genap.")

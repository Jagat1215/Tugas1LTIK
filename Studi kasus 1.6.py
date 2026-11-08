# Nama : Jagadditya K
# NIM : 2601673

nama = input("Masukkan nama siswa: ")
nilai = int(input("Masukkan nilai: "))

print("= HASIL PENILAIAN =")
print("Nama:", nama)
print("Nilai:", nilai)

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid!")
elif nilai >= 90:
    print("Nilai: A")
    print("Keterangan: Sangat Baik")
elif nilai >= 80:
    print("Nilai: B")
    print("Keterangan: Baik")
elif nilai >= 70:
    print("Nilai: C")
    print("Keterangan: Cukup")
elif nilai >= 60:
    print("Nilai: D")
    print("Keterangan: Kurang")
else:
    print("Nilai: E")
    print("Keterangan: Tidak Lulus")

if 0 <= nilai <= 100:
    if nilai >= 70:
        print("Status: LULUS")
    else:
        print("Status: TIDAK LULUS")
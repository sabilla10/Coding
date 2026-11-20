a = int(input("Masukkan angka A: "))
b = int(input("Masukkan angka B: "))
c = int(input("Masukkan angka C: "))

max_num = 0

if a > b:
    max_num = a
else:
    max_num = b

if c > max_num:
    max_num = c

print("Nilai terbesar adalah:", max_num)
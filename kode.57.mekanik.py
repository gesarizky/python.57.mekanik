# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput
m = int(input("Masukan Nilai Massa Benda (M) : "))
g = int(input("Masukan Nilai Gravitasi (g): "))
h = int(input("Masukan Nilai Ketinggian Benda (h): "))
v = int(input("Masukan Nilai Kecepatan (v): "))

# Mengkonversi
em = (m * g * h) + (0.5 * m * (v * v))

# Menampilkan Hasil
print('==========================================================')
print('Maka Hasil Energi Potensial (Ep) = ',em)
print('==========================================================')

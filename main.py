# Import library
import pandas as pd
import numpy as np

# Baca data dari tabel
data = pd.DataFrame({
    'Ukuran': [510, 550, 620, 630, 655, 700, 780, 800, 920, 1000],
    'Lantai': [4, 7, 9, 5, 8, 4, 10, 12, 14, 9],
    'Tarif Internet': [8, 50, 7, 24, 100, 8, 7, 50, 8, 24],
    'Harga Sewa': [320, 385, 400, 392, 380, 410, 480, 600, 570, 620]
})

# Tambahkan kolom X^2, Y^2, dan XY
data['X^2'] = data['Ukuran'] ** 2
data['Y^2'] = data['Harga Sewa'] ** 2
data['XY'] = data['Ukuran'] * data['Harga Sewa']

# Hitung total dari masing-masing kolom
total_x_squared = np.sum(data['X^2'])
total_y_squared = np.sum(data['Y^2'])
total_xy = np.sum(data['XY'])
total_ukuran = np.sum(data['Ukuran'])
total_harga_sewa = np.sum(data['Harga Sewa'])
n = len(data)

# Hitung nilai a (konstanta) dan b (koefisien)
a = (total_harga_sewa * total_x_squared - total_ukuran * total_xy) / (n * total_x_squared - total_ukuran**2)
b = (n * total_xy - total_ukuran * total_harga_sewa) / (n * total_x_squared - total_ukuran**2)

# Tampilkan nilai a dan b
print("Nilai a (konstanta):", a)
print("Nilai b (koefisien):", b)

# Prediksi harga sewa untuk ukuran 730 m^2
ukuran_baru = 730
harga_sewa_prediksi = a + b * ukuran_baru
print("Prediksi harga sewa untuk ukuran 730 m^2:", harga_sewa_prediksi)

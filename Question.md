## **Tugas Kelompok ke-3 - Week 8**

------

| Topik     | :    | Regresi Linear dan Regresi Logistik |
| --------- | ---- | ----------------------------------- |
| Sub topik | :    | Regresi Linear                      |


Tugas kelompok yang ketiga adalah berdasarkan data tabel, bantulah pemilik Gedung APN Tower menggunakan metode regresi linear untuk membuat prediksi harga sewa perbulan jika terdapat penambahan data baru ukuran ruang kantor sebesar 730 m2. 

| No   | Ukuran | Lantai | Tarif Internet | Tipe Bangunan | Harga Sewa |
| ---- | ------ | ------ | -------------- | ------------- | ---------- |
| 1    | 510    | 4      | 8              | C             | 320        |
| 2    | 550    | 7      | 50             | A             | 385        |
| 3    | 620    | 9      | 7              | C             | 400        |
| 4    | 630    | 5      | 24             | B             | 392        |
| 5    | 655    | 8      | 100            | A             | 380        |
| 6    | 700    | 4      | 8              | C             | 410        |
| 7    | 780    | 10     | 7              | C             | 480        |
| 8    | 800    | 12     | 50             | A             | 600        |
| 9    | 920    | 14     | 8              | C             | 570        |
| 10   | 1000   | 9      | 24             | B             | 620        |

Untuk memudahkan kelompok dalam melakukan prediksi harga, ikuti langkah-langkah sebagai berikut:

### Berdasarkan data tabel, tentukan variabel independen dan variabel dependen.

Jawab : 
Variabel independen (X) adalah variabel yang dapat mempengaruhi atau menjelaskan variabel dependen. Dalam konteks ini, kita ingin menggunakan regresi linear untuk memprediksi harga sewa (variabel dependen) berdasarkan beberapa fitur atau atribut tertentu. Oleh karena itu:

- Variabel independen (X):
  - Ukuran (m2)
  - Lantai
  - Tarif Internet
- Variabel dependen (Y):
  - Harga Sewa

> Jadi, variabel independen (X) adalah Ukuran, Lantai, dan Tarif Internet, sedangkan variabel dependen (Y) adalah Harga Sewa.

### Kemudian tambah kolom pada tabel hasil perhitungan dari $X², Y², XY$ dan total dari masing-masingnya.

Berikut adalah tabel hasil perhitungan kolom tambahan \(X^2\), \(Y^2\), \(XY\), dan totalnya:

\[
\begin{array}{|c|c|c|c|c|c|c|}
\hline
\text{No} & \text{Ukuran} & \text{Lantai} & \text{Tarif Internet} & \text{Harga Sewa} & X^2 & Y^2 & XY \\
\hline
1 & 510 & 4 & 8 & 320 & 260100 & 16 & 4080 \\
2 & 550 & 7 & 50 & 385 & 302500 & 49 & 3850 \\
3 & 620 & 9 & 7 & 400 & 384400 & 81 & 5580 \\
4 & 630 & 5 & 24 & 392 & 396900 & 25 & 3150 \\
5 & 655 & 8 & 100 & 380 & 429025 & 64 & 5240 \\
6 & 700 & 4 & 8 & 410 & 490000 & 16 & 2800 \\
7 & 780 & 10 & 7 & 480 & 608400 & 100 & 7800 \\
8 & 800 & 12 & 50 & 600 & 640000 & 144 & 9600 \\
9 & 920 & 14 & 8 & 570 & 846400 & 196 & 7360 \\
10 & 1000 & 9 & 24 & 620 & 1000000 & 81 & 9000 \\
\hline
\text{Total} & - & - & - & - & 5719729 & 781 & 60480 \\
\hline
\end{array}
\]

Keterangan:
- \(X^2\) merupakan kolom yang berisi hasil dari kuadrat setiap nilai pada kolom Ukuran.
- \(Y^2\) merupakan kolom yang berisi hasil dari kuadrat setiap nilai pada kolom Harga Sewa.
- \(XY\) merupakan kolom yang berisi hasil perkalian setiap nilai pada kolom Ukuran dengan nilai pada kolom Harga Sewa.
- Total \(X^2\), \(Y^2\), dan \(XY\) adalah jumlah dari masing-masing kolom.
  

### Gunakan model regresi linear sebagai berikut $Y = a + bX.$

### Lalu hitunglah nilai a menggunakan rumus  : (mencari nilai konstanta a)

$a = \frac{(\sum y)(\sum x^2) - (\sum x)(\sum xy)}{n(\sum x^2) - (\sum x)}$

### Cari pula nilai b menggunakan rumus : (mencari nilai koefisien b)

$b = \frac{n(\sum xy) - (\sum x)(\sum y)}{n(\sum x^2) - (\sum x)^2}$

### Buat **pseudocode** untuk penyelesaian kasus diatas menggunakan sintaks Python


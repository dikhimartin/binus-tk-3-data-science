**Tugas Kelompok ke-3 - Week 8**

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

1. Berdasarkan data tabel, tentukan variabel independen dan variabel dependen.

2. Kemudian tambah kolom pada tabel hasil perhitungan dari $X², Y², XY$ dan total dari masing-masingnya.

3. Gunakan model regresi linear sebagai berikut $Y = a + bX.$

4. Lalu hitunglah nilai a menggunakan rumus  : (mencari nilai konstanta a)

   $a = \frac{(\sum y)(\sum x^2) - (\sum x)(\sum xy)}{n(\sum x^2) - (\sum x)}$

5. Cari pula nilai b menggunakan rumus : (mencari nilai koefisien b)
   $b = \frac{n(\sum xy) - (\sum x)(\sum y)}{n(\sum x^2) - (\sum x)^2}$

6. Buat **pseudocode** untuk penyelesaian kasus diatas menggunakan sintaks Python


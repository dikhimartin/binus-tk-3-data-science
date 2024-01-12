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

### 1. Berdasarkan data tabel, tentukan variabel independen dan variabel dependen.

Jawab : 
Variabel independen (X) adalah variabel yang dapat mempengaruhi atau menjelaskan variabel dependen. Dalam konteks ini, kita ingin menggunakan regresi linear untuk memprediksi harga sewa (variabel dependen) berdasarkan beberapa fitur atau atribut tertentu. Oleh karena itu:

- Variabel independen (X):
  - Ukuran ruang kantor  (m²)
- Variabel dependen (Y):
  - Harga sewa perbulan

> Jadi, variabel independen (X) adalah Ukuran, sedangkan variabel dependen (Y) adalah Harga Sewa.

### 2. Kemudian tambah kolom pada tabel hasil perhitungan dari $X², Y², XY$dan total dari masing-masingnya.

| No    | Ukuran | Lantai | Tarif Internet | Harga Sewa | X²      | Y²      | XY      |
| ----- | ------ | ------ | -------------- | ---------- | ------- | ------- | ------- |
| 1     | 510    | 4      | 8              | 320        | 260100  | 102400  | 163200  |
| 2     | 550    | 7      | 50             | 385        | 302500  | 148225  | 211750  |
| 3     | 620    | 9      | 7              | 400        | 384400  | 160000  | 248000  |
| 4     | 630    | 5      | 24             | 392        | 396900  | 153664  | 246960  |
| 5     | 655    | 8      | 100            | 380        | 429025  | 144400  | 248900  |
| 6     | 700    | 4      | 8              | 410        | 490000  | 168100  | 287000  |
| 7     | 780    | 10     | 7              | 480        | 608400  | 230400  | 374400  |
| 8     | 800    | 12     | 50             | 600        | 640000  | 360000  | 480000  |
| 9     | 920    | 14     | 8              | 570        | 846400  | 324900  | 524400  |
| 10    | 1000   | 9      | 24             | 620        | 1000000 | 384400  | 620000  |
| Total | 7165   | -      | -              | 4557       | 5357725 | 2176489 | 3404610 |

- Menghitung Total dari Masing-Masing Kolom : 

  $\text{Total}(\sum X^2) = 5357725$

  $\text{Total}(\sum Y^2) = 2176489$

  $\text{Total}(\sum XY) = 3404610$

  $\text{Total}(\sum X) = 7165$

  $\text{Total}(\sum Y) = 4557$

  $n = 10$

- Keterangan:

  - $X²$ merupakan kolom yang berisi hasil dari kuadrat setiap nilai pada kolom Ukuran.

  - $Y²$ merupakan kolom yang berisi hasil dari kuadrat setiap nilai pada kolom Harga Sewa.

  - $XY$ merupakan kolom yang berisi hasil perkalian setiap nilai pada kolom Ukuran dengan nilai pada kolom Harga Sewa.

  - Total $X^2$$(Y^2)$, dan$(XY)$adalah jumlah dari masing-masing kolom.
    


### 3. Gunakan model regresi linear sebagai berikut $Y = a + bX.$

Dalam regresi linear, \(Y\) adalah variabel dependen (Harga Sewa), \(X\) adalah variabel independen (Ukuran), dan \(a\) serta \(b\) adalah parameter model yang perlu diestimasi. Model regresi linear dapat diwujudkan dalam bentuk persamaan:

$Y = a + bX$

di mana:

- \( Y \) adalah harga sewa,
- \( X \) adalah ukuran ruang kantor, dan
- \( a \) dan \( b \) adalah parameter yang perlu diestimasi.

### 4. Lalu hitunglah nilai a menggunakan rumus  : (mencari nilai konstanta a)
- Rumus a

   $a = \frac{(\sum y)(\sum x^2) - (\sum x)(\sum xy)}{n(\sum x^2) - (\sum x)}$


- Penyelesaian : 

  $a = \frac{(\sum Y)(\sum X^2) - (\sum X)(\sum XY)}{n(\sum X^2) - (\sum X)^2}$

  $a = \frac{(4557)(5357725) - (7165)(3404610)}{10(5357725) - (7165)^2}$

  $a = \frac{24415152825 - 24394030650}{53577250 - 51337225}$

  $a = \frac{21122175}{2240025}$

  $a \approx 9.42$


### 5. Cari pula nilai b menggunakan rumus : (mencari nilai koefisien b)

- Rumus b

   $b = \frac{n(\sum xy) - (\sum x)(\sum y)}{n(\sum x^2) - (\sum x)^2}$


- Penyelesaian : 

  $b = \frac{n(\sum XY) - (\sum X)(\sum Y)}{n(\sum X^2) - (\sum X)^2}$

  $b = \frac{10(3404610) - (7165)(4557)}{10(5357725) - (7165)^2}$

  $b = \frac{34046100 - 32650905}{53577250 - 51337225}$

  $b = \frac{1395195}{2240025}$

  $b \approx 0.62$


### 6. Buat **pseudocode** untuk penyelesaian kasus diatas menggunakan sintaks Python

Proses pseudocode terkait analisis regresi linear untuk prediksi harga sewa, dapat dilihat dokumentasi notebook nya di link sebagai berikut : 
https://github.com/dikhimartin/binus-tk-3-data-science/blob/master/linear-regresion.ipynb

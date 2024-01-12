Tugas Kelompok 3 - Regresi Linear 
==================

Tugas kelompok ini menekankan penerapan Regresi Linear dalam konteks Data Science. Kelompok diminta untuk membantu pemilik Gedung APN Tower dalam membuat prediksi harga sewa perbulan berdasarkan ukuran ruang kantor. 

Data yang diberikan telah diolah dengan mengikuti langkah-langkah regresi linear, dan tugas selanjutnya adalah memprediksi harga sewa jika terdapat penambahan data baru dengan ukuran ruang kantor sebesar 730 m2. 

Langkah-langkah tersebut melibatkan penentuan variabel independen dan dependen, perhitungan nilai a dan b, serta penggunaan model regresi linear.

Berikut adalah hasil laporan dari investigasi kami :

https://github.com/dikhimartin/binus-tk-3-data-science/blob/master/report.md


Memulai
---------------
Saya merekomendasikan penggunaan Visual Studio Code untuk mengakses file `.ipynb`. karena sudah dilengkapi dengan Jupyter notebook dan terminal. Namun, jika Anda lebih suka menggunakan terminal + server jupyterlab, juga di perbolehkan. Silakan ikuti langkah-langkah berikut untuk menyiapkan envinronment agar dapat menjalankan file:

Mulailah dengan menginstal [Anaconda](https://www.anaconda.com/products/distribution) (atau [Miniconda](https://docs.conda.io/en/latest/miniconda.html)), [git](https://git-scm.com/downloads), 

Selanjutnya, clone repositori ini dengan membuka terminal dan mengetikkan perintah berikut (jangan ketik tanda $ pertama pada setiap baris, itu hanya menunjukkan bahwa ini adalah perintah terminal):

    $ git clone https://github.com/dikhimartin/binus-tk-3-data-science.git
    $ cd binus-tk-3-data-science

Selanjutnya, jalankan perintah-perintah berikut:

    $ conda env create -f environment.yml
    $ conda activate bol_datascience_course
    $ python -m ipykernel install --user --name=bol_datascience_course

Jika Anda tidak menggunakan Visual Studio Code, Anda perlu memulai Jupyter Lab untuk dapat membuka notebook ipynb.

    $ jupyter lab

Catatan :
 Untuk mengaktifkan environment ini, menggunakan

     $ conda activate bol_datascience_course

 Untuk menonaktifkan environment yang aktif , gunakan

     $ conda deactivate    

Referensi
--------
* [Hands-on Machine Learning with Scikit-Learn, Keras and TensorFlow (3rd edition)](https://homl.info/er3)

# BAB 1 PENDAHULUAN
## 1.1 Latar Belakang
Mahasiswa yang merantau untuk menempuh pendidikan di Universitas Udayana memerlukan tempat tinggal yang nyaman dan sesuai dengan kebutuhan mereka. Banyaknya pilihan kost di sekitar kampus sering kali membuat mahasiswa kesulitan dalam menentukan kost yang paling sesuai berdasarkan faktor jarak, harga, fasilitas, dan kualitas tempat tinggal.

Perkembangan teknologi memungkinkan pemanfaatan Sistem Pendukung Keputusan (Decision Support System/DSS) untuk membantu pengguna dalam memilih alternatif terbaik berdasarkan kriteria tertentu. Salah satu pendekatan yang dapat digunakan adalah struktur data Graph yang mampu merepresentasikan hubungan antar lokasi serta algoritma Dijkstra untuk menentukan jarak terpendek dari kampus menuju lokasi kost.

Berdasarkan permasalahan tersebut, dibuat sebuah aplikasi DSS Pemilihan Kost di sekitar Universitas Udayana menggunakan Python, Streamlit, dan Folium Maps. Sistem ini diharapkan dapat membantu mahasiswa memperoleh rekomendasi kost yang sesuai dengan kebutuhan secara cepat dan objektif.

## 1.2 Rumusan Masalah
1. Bagaimana menerapkan struktur data Graph pada sistem pemilihan kost?
2. Bagaimana menerapkan algoritma Dijkstra untuk mencari jarak terpendek dari kampus ke lokasi kost?
3. Bagaimana membangun sistem pendukung keputusan yang mampu memberikan rekomendasi kost berdasarkan harga, fasilitas,            rating, dan jarak?

## 1.3 Tujuan
1. Agar dapat menerapkan struktur data Graph pada sistem pemilihan kost.
2. Agar dapat mengimplementasikan algoritma Dijkstra untuk menentukan jarak terpendek dari kampus ke kost.
3. Agar dapat membangun sistem pendukung keputusan yang dapat memberikan rekomendasi kost sesuai kebutuhan pengguna.

## 1.4 Manfaat
1. Memberikan pemahaman mengenai penerapan struktur data graph dalam merepresentasikan hubungan antar lokasi kampus dan kost    sehingga memudahkan proses pencarian informasi lokasi.
2. Membantu pengguna mengetahui jarak terpendek dari Kampus Udayana menuju lokasi kost sehingga dapat mempertimbangkan          efisiensi waktu dan akses menuju kampus.
3. Membantu mahasiswa dalam menentukan pilihan kost yang sesuai berdasarkan kriteria harga, fasilitas, jarak, dan rating        sehingga proses pengambilan keputusan menjadi lebih cepat dan objektif.

# BAB 2 DASAR TEORI
## 2.1 Struktur Data Graph
Graph merupakan salah satu struktur data non-linear yang digunakan untuk merepresentasikan hubungan antara suatu objek dengan objek lainnya. Struktur data graph terdiri dari sekumpulan simpul (vertex atau node) dan sisi (edge) yang menghubungkan simpul-simpul tersebut. Graph banyak digunakan dalam berbagai bidang seperti jaringan komputer, sistem navigasi, media sosial, dan sistem informasi geografis.

Node merupakan titik yang mewakili suatu objek atau entitas, sedangkan edge merupakan hubungan yang menghubungkan dua node. Pada graph berbobot (weighted graph), setiap edge memiliki nilai atau bobot tertentu yang dapat merepresentasikan jarak, biaya, waktu, atau nilai lainnya.

Berdasarkan arah hubungan antar node, graph dibedakan menjadi dua jenis yaitu graph berarah (directed graph) dan graph tidak berarah (undirected graph). Pada graph berarah, hubungan antar node memiliki arah tertentu, sedangkan pada graph tidak berarah hubungan dapat dilalui ke dua arah. Selain itu, graph juga dapat diklasifikasikan menjadi graph berbobot (weighted graph) dan graph tidak berbobot (unweighted graph).

## 2.2 Decision Support System (DSS)
Decision Support System (DSS) atau Sistem Pendukung Keputusan merupakan sistem berbasis komputer yang dirancang untuk membantu proses pengambilan keputusan dengan memanfaatkan data, model, dan metode analisis tertentu. DSS berfungsi sebagai alat bantu bagi pengguna dalam mengevaluasi berbagai alternatif sehingga dapat menghasilkan keputusan yang lebih tepat dan objektif.

Tujuan utama DSS adalah membantu pengguna dalam menyelesaikan permasalahan yang bersifat semi terstruktur maupun tidak terstruktur. DSS tidak menggantikan peran pengambil keputusan, melainkan memberikan informasi dan rekomendasi yang dapat digunakan sebagai bahan pertimbangan dalam menentukan pilihan terbaik.

DSS memiliki beberapa karakteristik, yaitu mampu mengolah data dalam jumlah besar, mendukung proses analisis, memberikan alternatif solusi, serta memungkinkan interaksi langsung antara pengguna dengan sistem. Dengan karakteristik tersebut, DSS banyak diterapkan pada bidang pendidikan, kesehatan, bisnis, industri, dan pemerintahan.

Secara umum, DSS terdiri dari tiga komponen utama. Komponen pertama adalah data management yang berfungsi untuk menyimpan dan mengelola data yang digunakan oleh sistem. Komponen kedua adalah model management yang digunakan untuk melakukan proses analisis dan perhitungan terhadap data. Komponen ketiga adalah user interface yang berfungsi sebagai media interaksi antara pengguna dan sistem.

## 2.3 Algoritma Dijkstra
Algoritma Dijkstra merupakan algoritma pencarian jalur terpendek (shortest path algorithm) yang diperkenalkan oleh Edsger W. Dijkstra pada tahun 1956. Algoritma ini digunakan untuk mencari jalur dengan total bobot terkecil dari suatu titik awal menuju titik tujuan pada graph berbobot yang memiliki bobot non-negatif.

Prinsip kerja algoritma Dijkstra adalah memilih node yang memiliki jarak sementara paling kecil dari titik awal, kemudian memperbarui jarak ke node-node tetangganya. Proses tersebut dilakukan secara berulang hingga seluruh node dalam graph telah diproses dan diperoleh jalur terpendek menuju setiap node.

Langkah-langkah algoritma Dijkstra dimulai dengan menentukan node awal dan memberikan nilai jarak 0 pada node tersebut. Selanjutnya seluruh node lain diberi nilai tak hingga (∞). Algoritma kemudian memilih node dengan jarak terkecil, menghitung jarak baru ke node tetangganya, dan memperbarui nilai jarak apabila ditemukan jalur yang lebih pendek. Proses ini terus dilakukan hingga semua node telah dikunjungi.

Algoritma Dijkstra memiliki beberapa kelebihan, antara lain mampu menemukan jalur terpendek secara optimal, mudah diimplementasikan, dan memiliki tingkat akurasi yang tinggi pada graph berbobot non-negatif. Namun, algoritma ini memiliki keterbatasan yaitu kurang efektif untuk graph yang memiliki bobot negatif.

# BAB 3 ANALISIS dan PERANCANGAN
## 3.1 Analisis Masalah
Mahasiswa yang merantau untuk menempuh pendidikan di Universitas Udayana memerlukan tempat tinggal yang sesuai dengan kebutuhan dan kemampuan finansial. Banyaknya pilihan kost di sekitar kampus sering kali membuat mahasiswa kesulitan dalam menentukan pilihan yang tepat karena harus mempertimbangkan berbagai faktor seperti jarak, harga, fasilitas, dan kualitas kost.

Proses pencarian kost secara manual membutuhkan waktu yang cukup lama karena pengguna harus membandingkan setiap alternatif satu per satu. Selain itu, pengguna sering mengalami kesulitan dalam menentukan kost yang memiliki lokasi paling dekat dengan kampus serta sesuai dengan budget yang dimiliki.

Berdasarkan permasalahan tersebut, diperlukan sebuah Sistem Pendukung Keputusan (DSS) yang mampu membantu pengguna dalam memilih kost terbaik. Sistem ini memanfaatkan struktur data graph untuk merepresentasikan hubungan antar lokasi serta algoritma Dijkstra untuk menentukan jarak terpendek dari Kampus Udayana menuju lokasi kost.

## 3.3 Flowchart
```mermaid
flowchart TD

A([Mulai]) --> B[Pengguna memasukkan budget maksimum]
B --> C[Pengguna memilih fasilitas yang diinginkan]
C --> D[Sistem membangun graph berdasarkan data lokasi]
D --> E[Sistem menghitung jarak antar lokasi menggunakan rumus Haversine]
E --> F[Algoritma Dijkstra dijalankan untuk mencari jarak terpendek dari Kampus Udayana]
F --> G[Sistem melakukan penyaringan berdasarkan budget dan fasilitas]
G --> H[Sistem menghitung skor DSS setiap kost]
H --> I[Sistem mengurutkan kost berdasarkan skor terbaik]
I --> J[Sistem menampilkan rekomendasi kost]
J --> K[Sistem menampilkan peta lokasi dan jalur terpendek]
K --> L([Selesai])
```

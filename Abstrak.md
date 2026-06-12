
## Rumusan Masalah
1. Bagaimana menerapkan struktur data Graph pada sistem pemilihan kost?
2. Bagaimana menerapkan algoritma Dijkstra untuk mencari jarak terpendek dari kampus ke lokasi kost?
3. Bagaimana membangun sistem pendukung keputusan yang mampu memberikan rekomendasi kost berdasarkan harga, fasilitas,          rating, dan jarak?

# 🏠 DSS Pemilihan Kost — Universitas Udayana, Bali

Sistem pendukung keputusan (Decision Support System) untuk membantu mahasiswa memilih kost terbaik di sekitar Universitas Udayana, Jimbaran, Bali. Sistem menggunakan struktur data **Graph** dengan algoritma **Dijkstra** untuk mencari jalur terpendek dari kampus ke setiap kost, lalu memberikan rekomendasi berdasarkan kombinasi jarak, harga, dan rating.

---

## 🔧 Teknologi yang Digunakan

- **Python** — bahasa pemrograman utama
- **Streamlit** — framework untuk tampilan antarmuka web
- **Folium** — visualisasi peta interaktif berbasis OpenStreetMap
- **Struktur Data Graph** — Adjacency List (undirected weighted graph)
- **Algoritma Dijkstra** — pencarian jalur terpendek dari kampus ke kost

---

## 📐 Cara Kerja Sistem

1. Semua lokasi (kampus + kost) dimodelkan sebagai **node** dalam graph
2. Jarak antar node dihitung menggunakan rumus **Haversine** (jarak nyata GPS dalam km)
3. **Dijkstra** menghitung jarak terpendek dari Kampus Udayana ke semua kost
4. Sistem memfilter kost berdasarkan **budget** dan **fasilitas** yang dipilih user
5. Skor DSS dihitung dengan rumus:
   ```
   skor = (jarak × 0.4) + (harga/1.000.000 × 0.2) − (rating × 0.4)
   ```
6. Kost dengan **skor terkecil** = rekomendasi terbaik (dekat + rating tinggi)

---

## 🚀 Cara Instalasi dan Menjalankan

### Langkah 1 — Pastikan Python sudah terinstal
Buka Command Prompt, ketik:
```
python --version
```
Jika belum ada, download di: https://www.python.org/downloads/

---

### Langkah 2 — Install library yang dibutuhkan
```
pip install streamlit folium streamlit-folium pandas
```

---

### Langkah 3 — Simpan file
Simpan file `app.py` ke sebuah folder, contoh:
```
C:\struktur data\app.py
```

---

### Langkah 4 — Jalankan aplikasi
Buka Command Prompt, masuk ke folder tersebut, lalu jalankan:
```
cd "C:\struktur data"
streamlit run app.py
```

---

### Langkah 5 — Buka di browser
Streamlit akan otomatis membuka browser di:
```
http://localhost:8501
```
Jika tidak terbuka otomatis, salin URL tersebut dan buka manual di browser.

---

### Langkah 6 — Gunakan aplikasi
- Atur **budget maksimum** menggunakan slider di sidebar
- Pilih **fasilitas** yang diinginkan (WiFi, AC, Dapur, dll)
- Lihat rekomendasi kost yang muncul di panel kanan
- Klik marker di peta untuk melihat detail kost
- Lihat tabel Dijkstra di bagian bawah untuk analisis lengkap

---

### Menghentikan aplikasi
Tekan `Ctrl + C` di Command Prompt.

---

## 📁 Struktur File

```
struktur data/
├── app.py          ← Kode utama aplikasi
└── README.md       ← Dokumentasi ini
```

---

## 📊 Data

| Komponen | Detail |
|----------|--------|
| Node | 14 (1 kampus + 13 kost) |
| Edge | 91 (complete graph) |
| Bobot | Jarak nyata Haversine (km) |
| Harga kost | Rp 700.000 – Rp 2.000.000/bulan |
| Algoritma | Dijkstra O((V+E) log V) |

---

*Project Mata Kuliah Struktur Data — Implementasi Graph sebagai DSS*

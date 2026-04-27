# 🎬 Simulasi Animasi Queue (Struktur Data)

Proyek ini berisi implementasi **simulasi animasi Queue (Antrian)** berdasarkan materi Struktur Data & Algoritma.  
Setiap kasus divisualisasikan dalam bentuk output bertahap (step-by-step) sehingga menyerupai animasi di terminal.

---

## 📌 Daftar Kasus

### 1. 🖨️ Queue Printer
Simulasi antrian dokumen pada printer:
- Dokumen masuk ke antrian (enqueue)
- Printer mencetak sesuai urutan (FIFO)
- Visualisasi perubahan queue

---

### 2. 🎮 Hot Potato (Circular Queue)
Simulasi permainan oper bola:
- Pemain berada dalam lingkaran
- Bola dipindahkan beberapa kali
- Pemain terakhir tersingkir
- Berjalan sampai tersisa pemenang

---

### 3. 🏥 Antrian Rumah Sakit (Priority Queue)
Simulasi pelayanan pasien:
- Pasien memiliki tingkat prioritas
- Prioritas lebih tinggi dilayani lebih dulu
- Jika sama → FIFO

---

### 4. 🌐 BFS (Breadth-First Search)
Simulasi traversal graf:
- Menggunakan Queue
- Menelusuri node per level
- Menampilkan proses kunjungan node

---

## ⚙️ Teknologi yang Digunakan

- Python 3
- Library standar:
  - `collections` (deque)
  - `heapq`
  - `time`

---

## ▶️ Cara Menjalankan

1. Pastikan Python sudah terinstall
2. Jalankan file Python:

```bash
python nama_file.py

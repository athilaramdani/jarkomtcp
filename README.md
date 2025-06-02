# Tugas Besar Jaringan Komputer Genap 2024/2025

## Tema: Web Server Berbasis TCP dengan Socket Programming

Repositori ini berisi tiga file utama untuk membangun dan menguji sebuah web server berbasis TCP:

* `client.py` : Klien TCP yang mengirimkan HTTP request.
* `server_single.py` : Web server sederhana yang hanya melayani satu klien pada satu waktu.
* `server_multi.py` : Versi multithreaded dari server untuk melayani beberapa klien secara bersamaan.

---

## Penjelasan Singkat

### `client.py`

* Klien menghubungi server menggunakan IP dan port tertentu.
* Mengirimkan permintaan HTTP GET ke server untuk mengambil sebuah file.
* Menampilkan hasil response dari server (isi file atau pesan error).

### `server_single.py`

* Hanya melayani satu koneksi klien dalam satu waktu.
* Menerima permintaan file dan mengirimkannya jika ditemukan.
* Jika file tidak ada, server akan merespons dengan 404 Not Found.

### `server_multi.py`

* Menggunakan threading untuk menangani beberapa koneksi klien sekaligus.
* Setiap koneksi akan dibuat dalam thread terpisah agar bisa paralel.

---

## Cara Pengujian

### 1. Siapkan File HTML

Letakkan file HTML contoh seperti `HelloWorld.html` di folder yang sama dengan file server (`.py`). Contoh isi file:

```html
<!DOCTYPE html>
<html>
  <head><title>Hello</title></head>
  <body><h1>Hello World!</h1></body>
</html>
```

### 2. Jalankan Server

```bash
# Untuk server single-threaded
python server_single.py

# Untuk server multithreaded
python server_multi.py
```

Server akan berjalan di port 6789 secara default. Pastikan firewall tidak memblokir port tersebut.

### 3. Jalankan Client

```bash
python client.py localhost 6789 HelloWorld.html
```

* `localhost` bisa diganti dengan IP server jika dari perangkat berbeda.
* `6789` adalah port yang digunakan oleh server.
* `HelloWorld.html` adalah file yang diminta.

Jika berhasil, isi HTML akan muncul di terminal. Jika file tidak ditemukan, akan muncul pesan `404 Not Found`.

---

## Catatan

* Server ini hanya mendukung HTTP GET sederhana.
* Semua file dijalankan via terminal menggunakan Python 3.
* Pastikan tidak ada server lain yang sedang menggunakan port 6789 saat pengujian.

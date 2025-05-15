
# TCP Web Server Project — Jaringan Komputer (Genap 2024/2025)

## Berkas

| File | Deskripsi |
|------|-----------|
| `server_single.py` | Server HTTP single‑threaded (menangani **1 koneksi** pada satu waktu) |
| `server_multi.py`  | Server HTTP multithreaded (membuat **1 thread per koneksi**) |
| `client.py`        | Klien HTTP sederhana untuk menguji server |

## Cara Menjalankan

```bash
# 1. Jalankan server (contoh port 6789)
python server_single.py 6789          # versi single‑thread
# atau
python server_multi.py 6789           # versi multithread
```

Letakkan file HTML (mis. `HelloWorld.html`) di **folder yang sama** dengan server.

```bash
# 2. Uji dengan browser
http://<IP‑SERVER>:6789/HelloWorld.html
```

**atau** gunakan klien bawaan:

```bash
# 3. Uji dengan client.py
python client.py <IP‑SERVER> 6789 HelloWorld.html
```

### Contoh

```bash
# Terminal 1
$ python server_multi.py 6789
[Multi] Listening on port 6789 ...

# Terminal 2
$ python client.py 127.0.0.1 6789 HelloWorld.html
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 52

<html><body><h1>Hello, world!</h1></body></html>
```

## Catatan

* Server *single‑thread* lebih sederhana tetapi mem‑block request lain sampai selesai.
* Server *multithread* membuat thread baru untuk setiap request — lebih responsif jika ada beberapa klien bersamaan.
* File selain `.html` juga bisa dilayani; `Content‑Type` otomatis diprediksi dengan modul `mimetypes`.

# ================ server_single.py ================
import socket, os, mimetypes          # modul wajib

def send_resp(c, path):               # kirim file/404
    path = '/index.html' if path == '/' else path
    f = '.' + path                    # path lokal
    if not os.path.isfile(f):         # kalau file ga ada
        body = b"<h1>404 Not Found</h1>"
        c.sendall(
            f"HTTP/1.1 404\r\nContent-Type:text/html\r\nContent-Length:{len(body)}\r\n\r\n"
            .encode() + body); return
    data = open(f, 'rb').read()       # baca file
    ct = mimetypes.guess_type(f)[0] or 'application/octet-stream'
    c.sendall(
        f"HTTP/1.1 200 OK\r\nContent-Type:{ct}\r\nContent-Length:{len(data)}\r\n\r\n"
        .encode() + data)

def main(port=8080):                  # fungsi utama
    s = socket.socket()               # bikin socket TCP
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port)); s.listen(1)   # dengar (backlog 1 cukup)
    print(f"[Single] nunggu 1 klien di {port}")
    c, addr = s.accept()              # terima satu klien
    print(f"[Single] layani {addr}")
    try:
        req = c.recv(1024).decode('iso-8859-1')  # baca request
        if not req: return
        method, path, _ = req.split()[:3]        # parse baris 1
        send_resp(c, path) if method == 'GET' else c.sendall(b"HTTP/1.1 405\r\n\r\n")
    except Exception as e:            # tangkap error
        c.sendall(f"HTTP/1.1 500\r\n\r\n{e}".encode())
    finally:
        c.close(); s.close()          # tutup klien & server
        print("[Single] tugas selesai, server mati")

if __name__ == '__main__':
    import sys; main(int(sys.argv[1]) if len(sys.argv) > 1 else 8080)

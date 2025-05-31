# ================= server_multi.py =================
import socket, os, mimetypes, sys          # modul core
from threading import Thread               # buat multi-thread

def send_resp(c, p):                       # kirim file / 404
    p = '/index.html' if p == '/' else p
    f = '.' + p
    if not os.path.isfile(f):
        body = b"<h1>404 Not Found</h1>"
        c.sendall(f"HTTP/1.1 404\r\nContent-Type:text/html\r\nContent-Length:{len(body)}\r\n\r\n".encode()+body); return
    d = open(f, 'rb').read()
    ct = mimetypes.guess_type(f)[0] or 'application/octet-stream'
    c.sendall(f"HTTP/1.1 200 OK\r\nContent-Type:{ct}\r\nContent-Length:{len(d)}\r\n\r\n".encode()+d)

def worker(c, a):                          # thread per klien
    print(f"[Multi] {a}")
    try:
        req = c.recv(1024).decode('iso-8859-1')
        if not req: return
        m, p, _ = req.split()[:3]
        if m != 'GET': c.sendall(b"HTTP/1.1 405\r\n\r\n"); return
        send_resp(c, p)
    except Exception as e:
        c.sendall(f"HTTP/1.1 500\r\n\r\n{e}".encode())
    finally: c.close()

def main(port=8080):                       # fungsi utama
    s = socket.socket(); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port)); s.listen()
    print(f"[Multi] Listen {port}")
    while True:
        c, a = s.accept()
        Thread(target=worker, args=(c, a), daemon=True).start()  # jalanin thread

if __name__ == '__main__': main(int(sys.argv[1]) if len(sys.argv) > 1 else 8080)

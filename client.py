# ================= client.py =================
import socket, sys                       # modul utama

def main():
    if len(sys.argv) != 4:                # cek argumen
        print('python client.py <HOST> <PORT> <FILE>'); return
    host, port, file = sys.argv[1], int(sys.argv[2]), sys.argv[3]  # ambil arg
    req = f"GET /{file} HTTP/1.1\r\nHost:{host}\r\nConnection:close\r\n\r\n"  # susun request
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   # buka socket
        s.connect((host, port))            # konek ke server
        s.sendall(req.encode())            # kirim request
        data = b''
        while True:                        # terima sampai habis
            chunk = s.recv(4096)
            if not chunk: break
            data += chunk
    print(data.decode('iso-8859-1', errors='replace'))  # tampilkan respon

if __name__ == '__main__': main()

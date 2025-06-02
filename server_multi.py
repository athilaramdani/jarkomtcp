import socket
import os
import threading

PORT = 6789  # Port server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", PORT))  # Bind ke semua IP
server_socket.listen(5)  # Listen dengan backlog 5 (multi)
print(f"Multithreaded server listening on port {PORT}...")

def handle_client(conn, addr):
    print(f"Handling client {addr}")
    request = conn.recv(1024).decode()  # Terima request dari client
    print(request)

    try:
        filename = request.split()[1][1:]  # Ambil nama file
        with open(filename, 'rb') as f:
            content = f.read()  # Baca file
        header = "HTTP/1.1 200 OK\r\n\r\n".encode()
        conn.send(header + content)  # Kirim header dan konten file
    except:
        msg = "HTTP/1.1 404 Not Found\r\n\r\nFile Not Found".encode()
        conn.send(msg)  # Kirim error jika file tidak ditemukan

    conn.close()  # Tutup koneksi

while True:
    conn, addr = server_socket.accept()  # Terima koneksi baru
    thread = threading.Thread(target=handle_client, args=(conn, addr))  # Buat thread baru
    thread.start()  # Mulai thread
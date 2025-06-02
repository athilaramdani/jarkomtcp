import socket
import os

PORT = 6789  # Port yang digunakan server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", PORT))  # Bind ke semua IP
server_socket.listen(1)  # Listen dengan backlog 1 (single request)
print(f"Server listening on port {PORT}...")

while True:
    conn, addr = server_socket.accept()  # Terima koneksi dari client
    print(f"Connection from {addr}")
    request = conn.recv(1024).decode()  # Terima request HTTP
    print(request)

    try:
        filename = request.split()[1][1:]  # Ambil nama file dari request
        with open(filename, 'rb') as f:
            content = f.read()  # Baca isi file
        header = "HTTP/1.1 200 OK\r\n\r\n".encode()
        conn.send(header + content)  # Kirim header dan konten file
    except:
        msg = "HTTP/1.1 404 Not Found\r\n\r\nFile Not Found".encode()
        conn.send(msg)  # Kirim error jika file tidak ditemukan

    conn.close()  # Tutup koneksi setelah respons selesai
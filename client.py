# client.py
import sys
import socket

server_host = sys.argv[1]  # IP address server dari argumen
server_port = int(sys.argv[2])  # Port server dari argumen
filename = sys.argv[3]  # Nama file yang diminta dari server

# Membuat socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))  # Koneksi ke server

# Mengirim request HTTP GET
request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
client_socket.send(request.encode())  # Kirim request ke server

# Terima respons dari server
response = b""
while True:
    data = client_socket.recv(1024)  # Terima data dalam blok 1024 byte
    if not data:
        break
    response += data

print(response.decode())  # Tampilkan hasil respons
client_socket.close()  # Tutup koneksi
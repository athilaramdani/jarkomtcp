import socket
import sys
import os
import mimetypes

def build_and_send_response(conn, path):
    if path == '/':
        path = '/index.html'

    filepath = '.' + path
    if not os.path.isfile(filepath):
        body = b"<h1>404 Not Found</h1>"
        header = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/html\r\n"
            f"Content-Length: {len(body)}\r\n"
            "\r\n"
        )
        conn.sendall(header.encode() + body)
        return

    with open(filepath, 'rb') as f:
        body = f.read()

    content_type = mimetypes.guess_type(filepath)[0] or 'application/octet-stream'
    header = (
        "HTTP/1.1 200 OK\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {len(body)}\r\n"
        "\r\n"
    )
    conn.sendall(header.encode() + body)

def handle_request(conn):
    try:
        request = conn.recv(1024).decode('iso-8859-1')
        if not request:
            return
        request_line = request.splitlines()[0]
        method, path, _ = request_line.split()
        if method != 'GET':
            conn.sendall(b"HTTP/1.1 405 Method Not Allowed\r\n\r\n")
            return
        build_and_send_response(conn, path)
    except Exception as e:
        error_msg = f"<h1>500 Internal Server Error</h1><pre>{e}</pre>".encode()
        header = (
            "HTTP/1.1 500 Internal Server Error\r\n"
            "Content-Type: text/html\r\n"
            f"Content-Length: {len(error_msg)}\r\n"
            "\r\n"
        )
        conn.sendall(header.encode() + error_msg)

def main():
    if len(sys.argv) != 2:
        print('Usage: python server_single.py <PORT>')
        sys.exit(1)

    port = int(sys.argv[1])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', port))
        server_socket.listen(1)
        print(f"[Single] Listening on port {port} ...")

        while True:
            conn, addr = server_socket.accept()
            print(f"[Single] Connection from {addr}")
            handle_request(conn)
            conn.close()

if __name__ == '__main__':
    main()

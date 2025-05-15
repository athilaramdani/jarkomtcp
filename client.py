import socket
import sys

def main():
    if len(sys.argv) != 4:
        print('Usage: python client.py <SERVER_HOST> <SERVER_PORT> <FILENAME>')
        sys.exit(1)

    host, port, filename = sys.argv[1], int(sys.argv[2]), sys.argv[3]

    request_line = f"GET /{filename} HTTP/1.1\r\n"
    headers = f"Host: {host}\r\nConnection: close\r\n\r\n"
    request = request_line + headers

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(request.encode())

        response = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data

    # Print raw HTTP response (header + body)
    print(response.decode('iso-8859-1', errors='replace'))

if __name__ == '__main__':
    main()

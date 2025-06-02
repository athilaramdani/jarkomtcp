import socket

def run_client():
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"  # Replace with the server's IP address
    server_port = 8000  # Replace with the server's port number

    # Establish connection with server
    try:
        client.connect((server_ip, server_port))
        print(f"Connected to server at {server_ip}:{server_port}")
    except ConnectionRefusedError:
        print(f"Connection failed: Server not running at {server_ip}:{server_port}")
        return

    # Send a request to the server to get the HTML content
    request = "GET /index.html HTTP/1.1\r\nHost: {}\r\n\r\n".format(server_ip)
    client.send(request.encode("utf-8"))

    # Receive the response from the server
    response = client.recv(4096).decode("utf-8")
    print(f"Received:\n{response}")

    # Close client socket (connection to the server)
    client.close()
    print("Connection to server closed")

def main():
    run_client()

if __name__ == "__main__":
    main()
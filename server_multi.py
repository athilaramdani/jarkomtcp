import socket
import threading

# Function to handle each client connection
def handle_client(client_socket, client_address):
    print(f"Connected by {client_address}")

    try:
        # Open and read the HTML file
        with open('index.html', 'r') as file:
            html_content = file.read()

        # Serve the HTML file to the client
        while True:
            request = client_socket.recv(1024)
            if not request:
                break

            request = request.decode("utf-8")
            print(f"Received: {request}")

            # If the client sends "close", close the connection
            if request.lower() == "close":
                client_socket.send("closed".encode("utf-8"))
                break

            # Send the HTML content
            client_socket.send(html_content.encode("utf-8"))

    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        print(f"Connection to {client_address} closed")
        client_socket.close()


def run_server():
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"
    port = 8000

    # Bind the socket to a specific address and port
    server.bind((server_ip, port))
    # Listen for incoming connections
    server.listen(5)
    print(f"Listening on {server_ip}:{port}")

    while True:
        # Accept incoming connections
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        # Create a new thread to handle the client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


def main():
    run_server()


if __name__ == "__main__":
    main()
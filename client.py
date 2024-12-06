import socket

# Function to handle the client
def start_client(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_host, server_port))
    print("Connected to server at {}:{}".format(server_host, server_port))

    while True:
        message = input("Client: ")  # Client sends message to server
        client_socket.send(message.encode())
        
        if message.lower() == 'exit':
            print("Connection closed.")
            break
        
        # Receive server's response
        response = client_socket.recv(1024).decode()
        print("Server: {}".format(response))

    client_socket.close()

if __name__ == "__main__":
    server_host = '127.0.0.1'  # Server IP address
    server_port = 12345  # Server port
    start_client(server_host, server_port)

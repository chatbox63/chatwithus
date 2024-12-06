
import socket

# Function to handle the server
def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server started. Waiting for connections on {}:{}...".format(host, port))

    # Accept client connection
    client_socket, client_address = server_socket.accept()
    print("Connection established with {}".format(client_address))

    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode()
        if message.lower() == 'exit':
            print("Connection closed by client.")
            break
        
        print("Client: {}".format(message))
        response = input("Server: ")  # Server sends message to client
        client_socket.send(response.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    host = '127.0.0.1'  # Localhost
    port = 12345  # Port to bind to
    start_server(host, port)

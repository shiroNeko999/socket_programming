import socket

def start_server(host='localhost', port=8576):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket
    server_socket.bind((host, port))
    
    # Listen for connections
    server_socket.listen(5)
    print(f"Listening on {host}:{port}")
    
    while True:  # Changed 'true' to 'True'
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        while True:  # Changed 'true' to 'True'
            data = client_socket.recv(1024)  # Receive data from the client
            if not data:
                break  # Exit loop if no data (client disconnected)
            
            client_socket.sendall(data)  # Send back the same data (echo)
        
        client_socket.close()  # Close the client socket after communication ends

if __name__ == "__main__":  # Changed 'main' to '__main__'
    start_server()

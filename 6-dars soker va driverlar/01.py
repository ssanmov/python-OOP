import socket

HOST = "127.0.0.1"
PORT = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    connection, address = server_socket.accept()
    with connection:
        print("Ulandi. Manzil: ", address)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data)
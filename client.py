import socket

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")

    client_socket.send(message.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')

    print("Message received from server: " + data)
    print("The no. of characters in the message is shown above along with the message in uppercase.")

    client_socket.close()

if __name__ == '__main__':
    client_program()
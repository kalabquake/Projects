import socket
import sys

def client_program():
    host = "192.168.1.10"  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    #message = input(" -> ")  # take input
    data=None
    with open(sys.argv[1],"rb") as f:
        data=f.read()
    #print(data)
    for x in data:
        #print(x)
        client_socket.send(bytes([x]))  # send message
        #input("press enter")
        #data = client_socket.recv(1024).decode()  # receive response

        #print('Received from server: ' + data)  # show in terminal

        #message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
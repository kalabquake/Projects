
import socket
import time

def server_program():
    # get the hostname
    name=input("Enter output name(with extension): ")
    host = "192.168.1.10"
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    recData=None
    t=time.time()
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024)
        if not data:
            # if data is not received break
            break
        #print(data)
        if(recData==None):
            recData=data
        else:
            recData+=data
    
    print(time.time()-t)
    with open(name,"wb") as f:
        f.write(recData)
     
        

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
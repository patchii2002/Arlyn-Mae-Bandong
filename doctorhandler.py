from codecs import decode
from threading import Thread
from doctor import Doctor
import  os.path
import pickle
BUFSIZE = 1024
CODE = "ascii"
class DoctorClientHandler(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client

    def run(self):
        self.filename = decode(self.client.recv(BUFSIZE), CODE)+ ".dat"
        if os.path.exists(self.filename):
            fileObj= open(self.filename, "rb")
            self.dr = pickle.load(fileObj)
        else:
            self.dr =Doctor()
        self.client.send(bytes(self.dr.greeting(),CODE))
        while True:
            message = decode(self.client.recv(BUFSIZE), CODE)
            if not message:
                print("Client Disconnected")
                self.client.close()
                fileObj= open(self.filename, "wb")
                pickle.dump(self.dr, fileObj)
                fileObj.close()
                break
            else:
                self.client.send(bytes(self.dr.reply(message), CODE))

doctorserver.py
from socket import *
from doctorclienthandler import DoctorClientHandler

HOST ="localhost"
PORT = 5000
ADDRESS =(HOST, PORT)
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)
while True:
    print("Waiting for connection...")
    client, address = server.accept()
    print("..connected from: ", address)
    handler = DoctorClientHandler(client)
    handler.start()

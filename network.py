import socket
import pickle

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = IPAddr
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode() #getting player number
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data)) #sending str data to the server
            return pickle.loads(self.client.recv(2048)) #receiving back obj data with loads
        except socket.error as e:
            print(e)
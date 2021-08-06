import socket

class Config():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SERVER = '10.3.168.135'
        PORT = 3000
        self.ADDR = (SERVER, PORT)
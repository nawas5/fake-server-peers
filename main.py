import socket
import json

# ipv4
import time

SERVER = '10.3.168.135'
PORT = 3000
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# time, name, x, y, z

with open('data/peers-log.json', 'r', encoding='utf-8') as f:
    mes = json.load(f)

server.listen()
print("Waiting")
conn, addr = server.accept()
print("[NEW CONNECTION]")

while True:
    for mes1 in mes:
        time.sleep(1)
        data2send = json.dumps(mes1).encode()
        conn.sendall(len(data2send).to_bytes(4, "little"))
        conn.sendall(data2send)







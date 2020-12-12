import socket

s = socket.socket()
print("Berjaya buat sokett")

port = 8888
addr= "192.168.43.2"
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', port))
print("Berjaya bind soket di port: " + str(port))

s.listen(5)
print("soket tengah menunggu client!")

while True:
        c, addr = s.accept()
        print("Dapat capaian dari: " + str(addr))

        c.send(b'Terima Kasih!')
        buffer = c.recv(1024)
        print(buffer)
c.close()




import socket

s = socket.socket()

PORT = 9090
print("\n Server akan dengar port dari:", PORT, "\n")

s.bind(('', PORT))

s.listen(10)

file = open("recv.txt", "wb") 
print("\n file maklumat akan di muatturun ke dalam  recv.txt server\n")

while True:
    
    conn, addr = s.accept()

    
    msg = "\n\n|______________________|\n Hai Client\n[IP address: "+ addr[0] + "], \n ֲֳ**SELAMAT DATANG KE Server** \n ->Server\n|______________________|\n \n\n"    
    conn.send(msg.encode())
    
    RecvData = conn.recv(1024)
    while RecvData:
        file.write(RecvData)
        RecvData = conn.recv(1024)

    file.close()
    print("\n File telah pun siap tiru \n")

    conn.close()
    print("\n tamat connection dari server \n")

    break

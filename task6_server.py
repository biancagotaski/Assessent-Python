import socket, os, pickle

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 7777

def file_dir(client):
    list_requests_info = os.listdir()
    ##adicionando para um dicionário, as informações do servidor para enviar ao cliente
    dictionary_info = {}
    for i in list_requests_info:
        if os.path.isfile(i): 
            dictionary_info[i] = []
            dictionary_info[i].append(os.stat(i).st_size)
            dictionary_info[i].append(os.stat(i).st_atime)
            dictionary_info[i].append(os.stat(i).st_mtime)
    dumps_bytes = pickle.dumps(dictionary_info)
    client.send(dumps_bytes)
    print('Enviando informacoes de arquivos para o cliente')

socket_server.bind((host, port))
socket_server.listen()
print(f'{host} está aguardando conexão na porta {port}')

(client, addr) = socket_server.accept()
print(f'O servidor esta conectado com: {str(addr)}')

while True:
    input_user = client.recv(1024)
    file_dir(client)

socket_server.close()
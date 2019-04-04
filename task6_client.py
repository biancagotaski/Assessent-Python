# Escreva um programa cliente e servidor sobre TCP em Python em que:
# - O cliente envia para o servidor o nome de um diretório e recebe 
# a lista de arquivos (apenas arquivos) existente nele.
# - O servidor recebe a requisição do cliente, captura o nome dos 
# arquivos no diretório em questão e envia a resposta ao cliente de volta.


import socket, pickle, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 7777

s.connect((host, port))

print('Digite "sair" a qualquer momento para sair da aplicacao')
input_user = input('Informe o diretório para saber a lista de arquivos pertencentes a ele:\n')

s.send(input_user.encode('utf-8'))

while input_user != 'sair':
    server = s.recv(1024)
    dictionary_from_server = pickle.loads(server)
    ##Pega cada item do dicionário vindo do servidor para exibir no cliente
    item_dict = '{:11}'.format("Tamanho")
    item_dict = item_dict + "Nome do arquivo"
    item_dict = item_dict + '{:27}'.format("Data de Criacao")
    item_dict = item_dict + '{:27}'.format("Data de Modificacao")
    print(item_dict)
    for item in dictionary_from_server:
        kb = dictionary_from_server[item][0]/1000
        size = '{:10}'.format(str('{:.2f}'.format(kb)+' KB'))
        print(size, time.ctime(dictionary_from_server[item][2]),
            " ", time.ctime(dictionary_from_server[item][1]), " ", item)
    ##faltou implementar o caso de o usuário não inserir nada no input.
    input_user = input('Informe o diretório para saber a lista de arquivos pertencentes a ele:\n')

s.send(input_user.encode('utf-8'))
s.close()
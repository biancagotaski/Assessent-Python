# Escreva um programa cliente e servidor sobre UDP em Python que:
# - O cliente envia para o servidor o pedido de obtenção da 
# quantidade total e disponível de memória no servidor e espera 
# receber a resposta durante 5s. Caso passem os 5s, faça seu 
# programa cliente tentar novamente mais 5 vezes 
# (ainda esperando 5s a resposta) antes de desistir.
# - O servidor repetidamente recebe a requisição do cliente, 
# captura a informação da quantidade total e disponível de memória
# há no servidor e envia a resposta ao cliente de volta.

import socket, psutil, pickle

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 7777))

print('Aguardando Conexao...')
package, destination = s.recvfrom(2048)

while True:
    package, destination = s.recvfrom(2048)
    print(f'Conectado com {destination}')
    print(f'{destination} solicitou informacoes sobre a memoria')
    print(destination)
    answer_client = []
    mem = psutil.virtual_memory()
    answer_client.append(mem.total)
    answer_client.append(mem.free)
    answer_in_bytes = pickle.dumps(answer_client)
    s.sendto(answer_in_bytes, destination)

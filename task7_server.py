import socket, psutil, pickle

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 7777))

print('Aguardando Conexao...')
package, destination = s.recvfrom(2048)

while True:
    package, destination = s.recvfrom(2048)
    print(f'Conectado com {destination}')
    print(f'{destination} solicitou informacoes sobre a memoria')
    # print(destination)
    # answer_client = []
    # mem = psutil.virtual_memory()
    # answer_client.append(mem.total)
    # answer_client.append(mem.free)
    # answer_in_bytes = pickle.dumps(answer_client)
    # s.sendto(answer_in_bytes, destination)

import socket, pickle, math, time

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.settimeout(0.005)
destination = (socket.gethostname(), 7777)
input_value = input('Digite:\
    \n1 - para exibir memoria total e disponivel do computador\
    \n2 - para sair da aplicacao\n')

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def start_connection():
    s.sendto(input_value.encode('utf-8'), destination)
    accepted = False
    check_time = False
    wait_for_server = time.time() + 60*5
    check_time = True
    for i in range(0,5):
        while not accepted:
            try:
                ACK, address = s.recvfrom(2048)
                accepted = True
            except socket.timeout:
                s.sendto(input_value.encode('utf-8'), destination)
                print('O servidor nao esta respondendo fechando a sessao')
                s.close()
    answer_server = pickle.loads(ACK)
    return answer_server

while input_value != '2':
    answer = start_connection()
    if input_value == '1':
        print (f'Memoria total: {convert_size(answer[0])}')
        print (f'Memoria disponivel: {convert_size(answer[1])}')
        input_value = input('Digite 1 para exibir as informacoes sobre memoria novamente ou 2 para sair\n')
    if input_value == '2':
        print('Saindo...')

print(f'{destination} encerrou a conexao...')
s.close()
# Dado um vetor A de tamanho N com apenas números inteiros positivos, 
# calcule o fatorial de cada um deles e armazene o resultado em um vetor B.
# Desenvolva o programa usando o módulo multiprocessing com 4 processos

import time, multiprocessing, psutil

vector_a = []
vector_b = []

def main():
    input_value = int(input('Insira o tamanho do array desejado: '))
    for i in range(input_value):
        vector_a.append(20)

def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)

def calcula_fatorial_do_vetor(entrada, saida):
    lista = entrada.get()
    for i in range(0,len(lista)):
        vector_b.append(fatorial(lista[i]))
    saida.put(lista)

def get_core_cpu():
  core_cpu = psutil.cpu_count()
  return core_cpu

if __name__ == "__main__":
    main()
    n_processos = 4
    tamanho = len(vector_a)
    fila_entrada = multiprocessing.Queue()
    fila_saida = multiprocessing.Queue()
    threads = []
    processos = []
    tempo_inicial = float(time.time())
    for i in range(n_processos):
        inicio = i*int(tamanho//n_processos)
        fim = (i+1)*int(tamanho//n_processos)
        fila_entrada.put(vector_a[inicio:fim])
        p = multiprocessing.Process(target = calcula_fatorial_do_vetor,args = (fila_entrada, fila_saida))
        p.start()
        processos.append(p)
    for t in processos:
        t.join()

    lista_final = []
    for p in processos:
        lista_final += fila_saida.get()
    # print(lista_final)
    tempo_final = float(time.time())
    tempo_total = tempo_final - tempo_inicial
    print('O tempo total de execução foi:', tempo_total)
    print('\nO número de cores do meu processador é:', get_core_cpu())